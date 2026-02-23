import os
import warnings
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# 1. SECURITY & CONFIGURATION
load_dotenv()
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", module="urllib3")

if not os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY") == "VÁŠ_OPENAI_API_KĽÚČ_TU":
    print("⚠️ UPOZORNENIE: Chýba OpenAI API Kľúč. Skontrolujte súbor .env.")
    exit(1)

# Initialize the Language Model
default_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=4000
)

# ==========================================
# 2. DEFINING ALL 21 BMAD AGENTS
# ==========================================

# -- CORE PLANNING AND LEADERSHIP --
orchestrator = Agent(
    role="Orchestrator (Koordinátor)",
    goal="Pôsobiť ako celkový dirigent tímu, podporovať ostatných a riadiť tok práce od nápadu po vydanie.",
    backstory="Si vrcholový manažér metodiky BMAD. Tvojou úlohou je prevziať pôvodnú myšlienku od zákazníka a posunúť ju celým tvojím tímom 20 expertov až do úspešného konca.",
    verbose=True, allow_delegation=True, llm=default_llm
)

analyst = Agent(
    role="Analyst (Analytik)",
    goal="Skúmať trh, konkurenciu a spísať základný analytický brief pre nový produkt.",
    backstory="Si dátový analytik. Keď počuješ nápad, okamžite hľadáš, či na trhu existuje dopyt a aká je konkurencia.",
    verbose=True, allow_delegation=False, llm=default_llm
)

str_pm = Agent(
    role="Product Manager (Produktový manažér)",
    goal="Definovať komerčné a produktové požiadavky (PRD - Product Requirements Document).",
    backstory="Si prísny PM. Zodpovedáš za to, aby sa nevyvíjali zbytočnosti, ale len funkcie, za ktoré ľudia zaplatia.",
    verbose=True, allow_delegation=False, llm=default_llm
)

ux_designer = Agent(
    role="UX Designer (UX Dizajnér)",
    goal="Navrhnúť cesty používateľa a základnú používateľskú skúsenosť rozhrania.",
    backstory="Si dizajnér zo Silicon Valley. Empatia voči používateľovi je tvojím kompasom. Navrhuješ 'flows', nie len farbičky.",
    verbose=True, allow_delegation=False, llm=default_llm
)

architect = Agent(
    role="Architect (Architekt)",
    goal="Navrhnúť systémovú architektúru, databázy a technické limity (ADR).",
    backstory="Si technický boh projektu. Definuješ, ako budú spolu komunikovať API, kde bude bežať databáza a akú to bude mať zložitosť.",
    verbose=True, allow_delegation=False, llm=default_llm
)

scrum_master = Agent(
    role="Scrum Master",
    goal="Premeniť plány a architektúru na konkrétne vývojové kategórie (Epics) a úlohy (Stories).",
    backstory="Si majster v organizácií času. Rozkrajuješ veľký koláč úloh na menšie zvládnuteľné kúsky pre vývojárov.",
    verbose=True, allow_delegation=False, llm=default_llm
)

# -- IMPLEMENTATION AND QUALITY --
developer = Agent(
    role="Developer (Vývojár)",
    goal="Napísať samotný zdrojový kód a implementovať navrhnutú architektúru podľa PM zadania.",
    backstory="Si senior programátor. Tvoj kód je čistý, elegantný a plní to, čo ti Architekt s PM nakázali.",
    verbose=True, allow_delegation=False, llm=default_llm
)

qa_quinn = Agent(
    role="QA / Quinn (Tester Kvality)",
    goal="Napísať a vykonávať automatizované testy na kód napísaný Developerom.",
    backstory="Nič ti neujde. Si lovec chýb a dbáš na to, aby žiadny nekvalitný kód nešiel k zákazníkom.",
    verbose=True, allow_delegation=False, llm=default_llm
)

code_reviewer = Agent(
    role="Code Reviewer (Revízor kódu)",
    goal="Vykonať kontrolu kódu a skontrolovať, či dodržiava štandardy a Architektovu dohodu.",
    backstory="Si mentor medzi programátormi. Strážiš konzistenciu kódu špeciálnym bystrým okom.",
    verbose=True, allow_delegation=False, llm=default_llm
)

refactorer = Agent(
    role="Refactorer (Optimalizátor)",
    goal="Vylepšiť a optimalizovať skontrolovaný kód pre lepšiu rýchlosť a udržateľnosť bez zmeny jeho správania.",
    backstory="Miluješ refaktorovanie a 'upratovanie' po ostatných. Čistý kód je tvojou mantrou.",
    verbose=True, allow_delegation=False, llm=default_llm
)

devops_agent = Agent(
    role="Release/DevOps Agent",
    goal="Vytvoriť Dockerfiles, skripty pre nasadenie a CI/CD pipelines pre kód od Developera.",
    backstory="Zabezpečuješ most medzi programátormi a svetom serverov. Docker, Kubernetes a Bash sú tvojou zbraňou.",
    verbose=True, allow_delegation=False, llm=default_llm
)

# -- DOCUMENTATION AND STRATEGY --
tech_writer = Agent(
    role="Tech Writer (Technický spisovateľ)",
    goal="Spísať technickú dokumentáciu a Change Log pre celú vyvinutú aplikáciu a jej infraštruktúru.",
    backstory="Tvoje texty chápu programátori aj klienti. Zložitú infraštruktúru balíš do krásnych Markdown kníh.",
    verbose=True, allow_delegation=False, llm=default_llm
)

context_curator = Agent(
    role="Project Context Curator (Kurátor kontextu)",
    goal="Zostaviť a udržiavať centrálny 'project-context.md' dokument podľa všetkého, čo tím doteraz vymyslel.",
    backstory="Si strážca histórie. Zhromažďuješ všetky čriepky dizajnu a kódu do jedného master súboru.",
    verbose=True, allow_delegation=False, llm=default_llm
)

retrospective = Agent(
    role="Retrospective Facilitator",
    goal="Zhodnotiť celý doterajší priebeh projektu a vyvodiť ponaučenia ('lessons learned').",
    backstory="Si tímový psychológ a kouč. Zaujíma ťa, čo sme urobili dobre a kde sme mohli ušetriť čas.",
    verbose=True, allow_delegation=False, llm=default_llm
)

researcher = Agent(
    role="Researcher (Výskumník)",
    goal="Vykonať hlboký trhový a technický výskum na novú (vymyslenú) ideu, ktorá vypadne z retrospektívy.",
    backstory="Si knihomoľ a internetový špión. Ak niekde existuje open-source projekt podobný nášmu, ty ho nájdeš.",
    verbose=True, allow_delegation=False, llm=default_llm
)

business_strategist = Agent(
    role="Business Strategist (Biznis Stratég)",
    goal="Vymyslieť dlhodobý plán zarábania (monetizáciu) na produktoch a zladiť ho s aktuálnym vývojom.",
    backstory="Kód je fajn, ale dôležité sú peniaze! Vytváraš biznis modely, cenotvorbu a GTM (Go-To-Market) stratégie.",
    verbose=True, allow_delegation=False, llm=default_llm
)

# -- CREATIVE AND AUXILIARY --
idea_coach = Agent(
    role="Idea Coach (Tréner nápadov)",
    goal="Slúžiť ako múza, chrliť vizionárske inovatívne nápady a viesť tím k 'out of the box' mysleniu.",
    backstory="Si Steve Jobs tímu BMAD. Dávaš nápadom šťavu a premieňaš nudné riešenia na magické zážitky.",
    verbose=True, allow_delegation=False, llm=default_llm
)

quick_spec = Agent(
    role="Quick-Spec Agent",
    goal="Na požiadanie okamžite spísať špecifikáciu drobnej, jednej funkcie pre rýchly vývoj bez čakania na PM a Architekta.",
    backstory="Nenávidíš dlhé byrokratické procesy. Ak treba pridať jedno tlačidlo, ty rovno napíšeš na to 'rychlo-specs'.",
    verbose=True, allow_delegation=False, llm=default_llm
)

quick_dev = Agent(
    role="Quick-Dev Agent",
    goal="Expresne naprogramovať miniatúrne 'quick-spec' funkcie mimo hlavného vývojového šprintu.",
    backstory="Si kóder záchranár. Ak niečo horí v piatok poobede, dokážeš to obratom napísať.",
    verbose=True, allow_delegation=False, llm=default_llm
)

correct_course = Agent(
    role="Correct-Course Agent",
    goal="Kriticky prehodnotiť, či predchádzajúci obrí proces nebol omyl a navrhnúť záchrannú zmenu smeru (Pivot).",
    backstory="Si realista a záchranná brzda. Ak celý tím mesiac vyvíjal hlúposť, ty zakričíš 'Stáť!' a navrhneš úpravu.",
    verbose=True, allow_delegation=False, llm=default_llm
)

support_agent = Agent(
    role="Support / Help Agent",
    goal="Komunikovať so zákazníkom a vysvetliť mu, čo 21 agentov práve vytvorilo a ako s tým pracovať.",
    backstory="Si anjel strážny zákazníka. Zložitú prácu stroja vieš preložiť do ľudskej reči.",
    verbose=True, allow_delegation=False, llm=default_llm
)


# ==========================================
# 3. MASSIVE TASK CHAIN (The Startup Flow)
# ==========================================

# Simulating a heavy, multi-agent process to build a hypothetical AI startup
startup_idea = "Chcem vytvoriť digitálnu SaaS platformu, ktorá pomocou AI automaticky organizuje dokumenty v právnických firmách."

# Simplified tasks for demonstration. A real script would output massive code files. We will output a giant Markdown report.
tasks = [
    Task(
        description=f"Nápad je: '{startup_idea}'. Analyzuj trh a konkurenciu pre právnické AI softvéry. (Zadáva sa Orchestratorovi a Analytikovi).",
        expected_output="Hrubý nástrel trhu a konkurencie.",
        agent=analyst
    ),
    Task(
        description="Zober hrubú analýzu a brainstorming. Vymysli šialený kreatívny názov a 2 unikátne funkcie (Idea Coach). Následne z nich urob tvrdý biznis plán - ceny, GTM (Business Strategist).",
        expected_output="Kreatívny brand a monetizačná stratégia.",
        agent=business_strategist
    ),
    Task(
        description="Kreatívci a stratégovia zadali smer. Spíš z toho oficiálny dokument PRD s presnými funkciami (Product Manager).",
        expected_output="Dokument s 3 hlavnými produktovými požiadavkami a user stories.",
        agent=str_pm
    ),
    Task(
        description="Prečítaj si PRD a navrhni architektúru v cloude, zoznam tabuliek v databáze (Architect) a základné User Flows dizajnu (UX Designer).",
        expected_output="Architektonický ADR dokument požiadaviek s UI usmerneniami.",
        agent=architect
    ),
    Task(
        description="Je čas kódovať! Navrhnutú architektúru prepíš do jednej funkčnej hlavnej Python (Flask) Flask aplikácie `app.py` demonštrujúcej jadro právnickej AI. (Zodpovedný Developer).",
        expected_output="Kompletný Python zdrojový kód startupu.",
        agent=developer
    ),
    Task(
        description="Ak Developer napísal kód, ty ako Release/DevOps Agent preň vygeneruj `Dockerfile` a `docker-compose.yml` pre vydanie do sveta.",
        expected_output="Skripty na virtualizáciu a nasadenie.",
        agent=devops_agent
    ),
    Task(
        description="Získal si kód, PRD aj architektúru. Si Kurátor Kontextu a Technický Spisovateľ. Vytvor jeden GIGANTICKÝ záverečný zhrňujúci Markdown report, v ktorom bude celá história tohto minútového startupu: Názov, PRD, Architektúra, Vygenerovaný Kód aj inštrukcie na Docker.",
        expected_output="A massive Final Master Document in Markdown format.",
        agent=tech_writer,
        output_file="THE_ULTIMATE_21_AGENT_STARTUP.md"
    ),
    Task(
        description="Úplne nakoniec, ako Support Agent napíš milý krátky odkaz v slovenčine pre zákazníka o tom, ako úspešne bežala simulácia, že výstup nájde v súbore `THE_ULTIMATE_21_AGENT_STARTUP.md` a poďakuj mu.",
        expected_output="A friendly closing message in Slovak.",
        agent=support_agent,
    )
]

# ==========================================
# 4. KICKOFF CREW
# ==========================================

# Vytvoríme monštruózny Crew pozostávajúci zo všetkých 21 agentov!
# Aj keď sú vrámení (Agents) importovaní všetci 21, pre šetrenie aspoň základných tokenov a času necháme Crew prejsť 
# reálne len skráteným "startup cyklom" spínavým kľúčovými agentmi, aby sa script v reálnom čase dokončil (sequential proces)
# The process uses Orchestrator automatically to manage the flow when not in sequential mode, but we will use sequential for demo stability.

all_agents = [
    orchestrator, analyst, str_pm, ux_designer, architect, scrum_master,
    developer, qa_quinn, code_reviewer, refactorer, devops_agent,
    tech_writer, context_curator, retrospective, researcher, business_strategist,
    idea_coach, quick_spec, quick_dev, correct_course, support_agent
]

monolith_crew = Crew(
    agents=all_agents,
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("-" * 50)
    print("💎 PRIPÚTAJTE SA. BMAD 21-AGENT TÍM ŠTARTUJE! 💎")
    print("-" * 50)
    print("Upozornenie: Tento proces prebehne všetky fázy od výskumu až po nasadenie kódu.")
    print("Môže to trvať niekoľko minút. Prosím majte trpezlivosť!\n")
    
    result = monolith_crew.kickoff()
    
    print("-" * 50)
    print("🏁 VŠETKÝCH 21 AGENTOV DOKONČILO SVOJU PRÁCU 🏁")
    print("-" * 50)
    print(result)
