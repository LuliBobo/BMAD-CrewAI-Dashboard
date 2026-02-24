import os
import sys
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

# Initialize the Language Model s tvrdým obmedzením tokenov (LOW-COST)
default_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1500  # Znížené zo 4000 pre šetrenie peňazí
)

# ==========================================
# 2. DEFINING ALL 21 BMAD AGENTS (Added max_iter=3)
# ==========================================


def load_agent_skills(filename):
    import os
    filepath = os.path.join(os.path.dirname(__file__), 'agent_skills', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    parts = text.split('# ')
    skills = {}
    for part in parts:
        part = part.strip()
        if not part:
            continue
        lines = part.split('\\n', 1)
        if len(lines) == 2:
            skills[lines[0].strip().lower()] = lines[1].strip()
    return skills

# -- CORE PLANNING AND LEADERSHIP --
orchestrator = Agent(**load_agent_skills("orchestrator.md"), verbose=True, allow_delegation=True, llm=default_llm, max_iter=3)
analyst = Agent(**load_agent_skills("analyst.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
str_pm = Agent(**load_agent_skills("str_pm.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
ux_designer = Agent(**load_agent_skills("ux_designer.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
architect = Agent(**load_agent_skills("architect.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
scrum_master = Agent(**load_agent_skills("scrum_master.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)

# -- IMPLEMENTATION AND QUALITY --
developer = Agent(**load_agent_skills("developer.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
qa_quinn = Agent(**load_agent_skills("qa_quinn.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
code_reviewer = Agent(**load_agent_skills("code_reviewer.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
refactorer = Agent(**load_agent_skills("refactorer.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
devops_agent = Agent(**load_agent_skills("devops_agent.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)

# -- DOCUMENTATION AND STRATEGY --
tech_writer = Agent(**load_agent_skills("tech_writer.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
context_curator = Agent(**load_agent_skills("context_curator.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
retrospective = Agent(**load_agent_skills("retrospective.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
researcher = Agent(**load_agent_skills("researcher.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
business_strategist = Agent(**load_agent_skills("business_strategist.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)

# -- CREATIVE AND AUXILIARY --
idea_coach = Agent(**load_agent_skills("idea_coach.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
quick_spec = Agent(**load_agent_skills("quick_spec.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
quick_dev = Agent(**load_agent_skills("quick_dev.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
correct_course = Agent(**load_agent_skills("correct_course.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)
support_agent = Agent(**load_agent_skills("support_agent.md"), verbose=True, allow_delegation=False, llm=default_llm, max_iter=3)

# ==========================================
# 3. MASSIVE TASK CHAIN (The Startup Flow) - Hierarchical
# ==========================================

# Predvolený nápad, ak je skript spustený bez argumentu
startup_idea = "Chcem vytvoriť digitálnu SaaS platformu, ktorá pomocou AI automaticky organizuje dokumenty v právnických firmách."

# Ak zachytíme argument z príkazového riadku (frontendu), prepíšeme nápad
if len(sys.argv) > 1:
    startup_idea = sys.argv[1]
    print(f"⚡ ZACHYTENÝ NOVÝ NÁPAD OD POUŽÍVATEĽA: '{startup_idea}'\n")

# Removed "agent=..." because in hierarchical process, the manager decides who takes which task!
tasks = [
    Task(
        description=f"Nápad je: '{startup_idea}'. Zisti, akí silní sú konkurenti ako Harvey AI a podobne. Spíš hrubý nástrel trhu a konkurencie pre nový právnický software.",
        expected_output="Hrubý nástrel trhu a konkurencie pre nový právnický software."
    ),
    Task(
        description="Zober hrubú analýzu a brainstorming. Vymysli šialený kreatívny názov značky a definuj tvrdý biznis plán - ceny a stratégie (Cenotvorba, GTM).",
        expected_output="Kreatívny brand a monetizačná stratégia."
    ),
    Task(
        description="Na základe názvu a monetizačnej stratégie spíš oficiálny dokument PRD. Dokument musí obsahovať 3 hlavné funkcie pre programátorov.",
        expected_output="Dokument s 3 hlavnými produktovými požiadavkami a user stories."
    ),
    Task(
        description="Prečítaj si PRD a navrhni architektúru aplikácie. Definuj zoznam tabuliek pre databázu (ADR dokument) a základné User Flows dizajnu do textovej podoby.",
        expected_output="Architektonický ADR dokument požiadaviek s UI usmerneniami."
    ),
    Task(
        description="Je čas kódovať! Navrhnutú architektúru prepíš do jednej funkčnej Flask aplikácie `app.py`. Nech kód simuluje aspoň 1 API pre uloženie právneho dokumentu.",
        expected_output="Kompletný Python zdrojový kód startupu."
    ),
    Task(
        description="Priprav skripty na virtuálne nasadenie python kódu. Súrne vygeneruj aspoň základný `Dockerfile` a `docker-compose.yml` pre aplikáciu z predchádzajúceho kroku.",
        expected_output="Skripty na virtualizáciu a nasadenie (Dockerfile, docker-compose)."
    ),
    Task(
        description="Získal si všetko úsilie tímu (PRD, Architektúra, Kódy, Dockerfile). Vytvor jeden gigantický záverečný zhrňujúci Markdown report s históriou startupu.",
        expected_output="A massive Final Master Document in Markdown format.",
        output_file="THE_ULTIMATE_HIERARCHICAL_STARTUP.md"
    ),
    Task(
        description="Úplne nakoniec aspoň 2 vetami poďakuj v slovenčine zákazníkovi, že úspešne bežala 21-agentová hierarchická simulácia, a podotkni, nech si prečíta finálny súbor.",
        expected_output="A friendly closing message in Slovak."
    )
]

# ==========================================
# 4. KICKOFF CREW
# ==========================================

# Vytvoríme monštruózny Crew pozostávajúci zo všetkých 21 agentov.
all_agents = [
    orchestrator, analyst, str_pm, ux_designer, architect, scrum_master,
    developer, qa_quinn, code_reviewer, refactorer, devops_agent,
    tech_writer, context_curator, retrospective, researcher, business_strategist,
    idea_coach, quick_spec, quick_dev, correct_course, support_agent
]

# Process.hierarchical nasadí vlastného Manažéra nad vštkých 21 ľudí.
# manager_llm zadefinuje lacný gpt-4o-mini pre jeho rozhodovacie chvíle.
monolith_crew = Crew(
    agents=all_agents,
    tasks=tasks,
    process=Process.hierarchical,
    manager_llm=default_llm,
    verbose=True
)

if __name__ == "__main__":
    print("-" * 50)
    print("💎 PRIPÚTAJTE SA. BMAD 21-AGENT TÍM ŠTARTUJE (HIERARCHICAL MODE)! 💎")
    print("-" * 50)
    print("Upozornenie: Manažér (LLM) práve prevzal 8 úloh a začne ich manažovať pre 21 podriadených.")
    print("Proces má zapnutú najsilnejšiu tokenovú low-cost optimalizáciu (max_iter=3, max_tokens=1500).")
    print("Môže to trvať niekoľko minút. Prosím majte trpezlivosť!\n")
    
    result = monolith_crew.kickoff()
    
    print("-" * 50)
    print("🏁 VŠETKÝCH 21 AGENTOV (S MANAŽÉROM V ČELE) DOKONČILO SVOJU PRÁCU 🏁")
    print("-" * 50)
    print(result)
