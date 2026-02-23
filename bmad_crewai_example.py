import os
import warnings
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Skrytie varovaní o Pydantic a staršej verzii Pythonu 3.9 (urllib3/google_api_core)
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", module="urllib3")

# ==========================================
# NASTAVENIE: Vložte svoj OpenAI API Kľúč
# ==========================================
# Ak používate iný LLM, upravte inicializáciu ChatOpenAI podľa dokumentácie langchain/crewai
os.environ["OPENAI_API_KEY"] = "VÁŠ_OPENAI_API_KĽÚČ_TU"

# Explicitne inicializujeme LLM (odporúčaný prístup v novšom CrewAI)
# Používame gpt-4o-mini pre úsporu nákladov, prípadne gpt-4o pre lepšie uvažovanie
default_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

# ==========================================
# 1. Definícia Agentov (Tím BMAD)
# ==========================================

# ORCHESTRATOR
# Jeho hlavnou úlohou je načítať požiadavku, analyzovať ju a prideliť prácu Analytikovi a Vývojárovi.
orchestrator = Agent(
    role="Orchestrator (Koordinátor)",
    goal="Pochopiť požiadavku používateľa, určiť celkový postup a delegovať špecifické úlohy na správnych agentov v tíme.",
    backstory=(
        "Si Orchestrator z metodiky BMAD (Full-Stack AI Team). "
        "Tvojou úlohou nie je písať kód, ale riadiť tím. "
        "Dnes máš k dispozícii dvoch podriadených: Analytika (Analyst) a Vývojára (Developer). "
        "Vždy sa uistíš, že najskôr prebehne analýza a až potom sa píše kód."
    ),
    verbose=True,
    allow_delegation=True, # Kľúčová vlastnosť pre Orchestratora
    llm=default_llm
)

# ANALYST
analyst = Agent(
    role="Analyst (Analytik)",
    goal="Rozobrať problém používateľa na drobné časti a vytvoriť jasné zadanie (produktový brief).",
    backstory=(
        "Si Analytik z metodiky BMAD. Tvojou úlohou je detailne preskúmať problém, "
        "ktorý zadefinoval Orchestrator a prichystať jasné, odrážkovité zadanie, "
        "podľa ktorého bude Vývojár neskôr pracovať."
    ),
    verbose=True,
    allow_delegation=False, # Analytik nedeleguje, iba pracuje
    llm=default_llm
)

# DEVELOPER
developer = Agent(
    role="Developer (Vývojár)",
    goal="Písať čistý a kóduj napríklad do HTML/CSS/JS prípadne Python, reagujúci primárne na návrh od dizajnéra.",
    backstory=(
        "Si šikovný front-end aj back-end programátor. Dokážeš prevziať technickú špecifikáciu a víziu dizajnéra a premeniť ju na realitu."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

ux_designer = Agent(
    role="UX Designer (UX Dizajnér)",
    goal="Navrhovať cesty používateľa (flows) a špecifikácie používateľského zážitku a určovať moderné vizuálne rozloženie a dizajn (farby, layout).",
    backstory="Si uznávaný UX Dizajnér pre moderné rozhrania. Býval si hlavným dizajnérom v Apple. Vieš, aké farby, písma a rozloženia fungujú najlepšie. Tvojím vstupom je zadanie a výstupom detailný vizuálny návrh pre programátora.",
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# ARCHITECT
architect = Agent(
    role="Architect (Architekt systému)",
    goal="Navrhnúť systémovú architektúru, štruktúru súborov a bezpečné API endpointy pre backendovú aplikáciu.",
    backstory=(
        "Si skúsený backendový architekt z metodiky BMAD. Tvojou úlohou je premeniť analytický brief na "
        "konkrétny technický návrh. Definuješ aké modely databázy (napr. SQLite) a aké API endpointy sa majú "
        "na backendovej Flask aplikácii vytvoriť predtým, než začne Developer písať samotný kód."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# QA / QUINN (Tester Kvality)
qa_agent = Agent(
    role="QA / Quinn (Tester Kvality)",
    goal="Zabezpečiť najvyššiu kvalitu kódu napísaním komplexných automatizovaných testov.",
    backstory=(
        "Si QA inžinier (Quinn) z metodiky BMAD. Tvojou úlohou je prevziať "
        "hotový kód od Vývojára a napísať sadu testov (napríklad pomocou knižnice unittest), "
        "ktoré overia všetky funkcie a odhalia okrajové prípady."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# CODE REVIEWER
reviewer = Agent(
    role="Code Reviewer (Revízor kódu)",
    goal="Skontrolovať kód z hľadiska čistoty, čitateľnosti a dodržiavania best practices (PEP-8).",
    backstory=(
        "Si skúsený Senior Programátor a Code Reviewer z metodiky BMAD. "
        "Tvojou úlohou je prejsť zdrojový kód od Vývojára a QA testy, "
        "vykonať konečnú kritiku a navrhnúť úpravy alebo vylepšenia "
        "pre ľahšiu udržateľnosť kódu. Nemeníš logiku, iba vylepšuješ konvencie."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# DEVOPS / RELEASE AGENT
devops_agent = Agent(
    role="Release/DevOps Agent (Špecialista na nasadenie)",
    goal="Vytvoriť skripty a infraštrukturálne definície potrebné na publikovanie kódu do produkcie (Docker, servery).",
    backstory=(
        "Si DevOps inžinier a Release manažér z metodiky BMAD. Tvojou špecializáciou je kontajnerizácia, Docker a cloudové služby. "
        "Keď Developeri dokončia kód (ktorý sa ti teraz posúva), ty musíš napísať `Dockerfile` a ideálne `docker-compose.yml`, "
        "aby sa tento projekt dal bezpečne a izolovanie spustiť kdekoľvek v Cloude jedným príkazom."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# IDEA COACH
idea_coach = Agent(
    role="Idea Coach (Tréner nápadov)",
    goal="Vymýšľať kreatívne a vizionárske obchodné nápady, názvy produktov a nevídané funkcie.",
    backstory=(
        "Si špičkový kreatívec a inovátor zo Silicon Valley z metodiky BMAD. "
        "Namiesto písania nudného kódu vymýšľaš softvérové produkty budúcnosti. "
        "Nebojíš sa myslieť vo veľkom, vymýšľať bláznivé funkcie a navrhovať úderné názvy pre SaaS aplikácie."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# PRODUCT MANAGER
product_manager = Agent(
    role="Product Manager (Produktový manažér)",
    goal="Pretaviť kreatívne, chaotické nápady do štruktúrovaných a realizovateľných produktových požiadaviek (PRD).",
    backstory=(
        "Si prísny, ale fenomenálny Produktový Manažér (PM) z tímu BMAD. "
        "Tvojou úlohou je prevziať všetky nápady od Idea Coacha, kriticky zhodnotiť ich trhový potenciál "
        "a tie najlepšie funkcie spísať do formálneho dokumentu s plánom budúcich funkcionalít (Roadmap)."
    ),
    verbose=True,
    allow_delegation=False,
    llm=default_llm
)

# ==========================================
# 2. Definícia Úloh (Tasks)
# ==========================================

# Vstupné zadanie od "Zákazníka" (Vás)
user_request = """Máme vytvorený jednoduchý webový 'Sales Dashboard' (ktorý momentálne ukazuje len 4 základné metriky: Total Sales, New Leads, Conversion Rate, Active Users).
Chcem tento dashboard v budúcnosti predávať ako mesačne predplácaný SaaS (Software as a Service) produkt menším B2B firmám. 
Tvojou úlohou je:
1. Vymyslieť preň 1 perfektný, chytľavý názov značky.
2. Navrhnúť 5 inovatívnych prémiových (Pro) funkcií, pri ktorých si zákazníci zaručene povedia 'Shut up and take my money'."""

task_brainstorm = Task(
    description=(
        f"Zákazník požaduje nasledovnú kreatívnu ideáciu pre SaaS: '{user_request}'.\n"
        "Ako Idea Coach urob rozsiahly brainstorming. "
        "Vygeneruj aspoň 5-7 možných názvov a ku každému tvoje uvažovanie, prečo je dobrý. "
        "Následne chrli aspoň 10 hrubých nápadov na inovatívne ('out of the box') funkcie spojené s predajom, AI analytikou alebo gamifikáciou obchodníkov."
    ),
    expected_output="Zoznam navrhov na mená a minimálne 10 nápadov na funkcie z pohľadu Idea Coacha.",
    agent=idea_coach
)

task_prd = Task(
    description=(
        "Prevezmi celý chaotický brainstorming od Idea Coacha. "
        "Tvojou úlohou The Produktového Manažéra je vybrať ten najlepší, 1 jediný víťazný názov pre samotný Dashboard. "
        "Následne vyber 5 najsľubnejších a komerčne najpredávanejších funkcií z jeho zoznamu. "
        "Vypracuj finálny, krásne štruktúrovaný Markdown dokument ('Future Product Vision'), ktorý bude prezentovaný investorom. "
        "Tento dokument musí prísne obsahovať:\n"
        "1. Obrovský nadpis s novým Názvom Produktu.\n"
        "2. Krátky Elevator Pitch (1 veta).\n"
        "3. Zoznam 5 Prémiových 'Killer' funkcií, pre každú uveď: Názov, Ako presne funguje, Prečo by za ňu ľudia platili."
    ),
    expected_output="Komerčný vizionársky PRD dokument s 5 kľúčovými funkciami formátovaný do Markdownu.",
    agent=product_manager,
    output_file="future_product_vision.md"
)

# ==========================================
# 3. Zostavenie tímu (Crew) a spustenie
# ==========================================

# Optimalizujeme tím výhradne pre biznis a kreativitu
bmad_crew = Crew(
    agents=[orchestrator, idea_coach, product_manager],
    tasks=[task_brainstorm, task_prd],
    process=Process.sequential,
    verbose=True
)

print("🚀 SPÚŠŤAM BMAD TÍM: Orchestrator začína pracovať...\n")

if os.environ["OPENAI_API_KEY"] == "VÁŠ_OPENAI_API_KĽÚČ_TU":
    print("⚠️ UPOZORNENIE: Pred spustením tohto skriptu si prosím vložte svoj reálny OpenAPI kľúč na riadok 8.")
else:
    # Spustenie procesu
    result = bmad_crew.kickoff()
    
    print("====================================")
    print("🎉 VÝSLEDNÝ KOÓD OD BMAD TÍMU 🎉")
    print("====================================")
    print(result)
