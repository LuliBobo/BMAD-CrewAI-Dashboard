# BMAD Method: Full-Stack AI Team

The BMAD Method ships with a full-stack AI team of 21 named agents. Each agent has a specific role in planning, building, and maintaining software and automations.

> **💡 Note on CrewAI Environment Requirements:** 
> When running this method via CrewAI locally on macOS with Python 3.9, you should stick to `crewai==0.1.32` and `pydantic==2.5.3`. Newer versions of `crewai` (> 0.28) use advanced `type | None` syntax, which crashes in Python 3.9. Deprecation warnings are hidden in the codebase (`bmad_crewai_example.py`) for a cleaner console experience.

## 🚀 Quick Start Guide (For New Developers)
Ak si sťahujete repozitár do nového počítača, pre naštartovanie Dashboardu a agentov postupujte takto:

**Krok 1: Klonovanie a vstup do repozitára**
```bash
git clone https://github.com/LuliBobo/BMAD-CrewAI-Dashboard.git
cd BMAD-CrewAI-Dashboard
```

**Krok 2: Inštalácia závislostí a knižníc**
```bash
pip install -r requirements.txt
```

**Krok 3: Nastavenie tajného API kľúča (.env)**
Z bezpečnostných dôvodov projekt neobsahuje kľúče, musíte si vytvoriť vlastný podľa šablóny:
```bash
cp .env.example .env
```
Následne otvorte vytvorený súbor `.env` a doplňte do neho Váš OpenAI kľúč: \`OPENAI_API_KEY=sk-...\`

**Krok 4: Spustenie Produkčného Webservera (Gunicorn)**
Aplikácia sa automaticky rozbehne lokálne aj s UI na porte 5000:
```bash
./start_bmad.sh
```
Aplikácia následne beží na `http://127.0.0.1:5000`.

## Core Planning and Leadership Agents

- **Orchestrator** - Overall conductor and help system. Routes work to the right agent and answers "how do I...?" questions.
- **Analyst** - Explores the problem space, runs brainstorming and research, and helps create the product brief.
- **Product Manager (PM)** - Owns the PRD, user needs, and success criteria.
- **UX Designer** - Designs flows and UX specs when user experience matters.
- **Architect** - Designs system architecture, writes ADRs, and defines technical constraints.
- **Scrum Master (SM)** - Turns plans into epics and stories, manages sprint status, and drives the development cycle.

## Implementation and Quality Agents

- **Developer (Dev)** - Implements stories, writes code and tests following project context and architecture.
- **QA / Quinn** - Built-in QA agent that generates and maintains automated tests.
- **Code Reviewer** - Performs structured code reviews against standards and architecture.
- **Refactorer** - Improves existing code for clarity, performance, and maintainability (often bundled in Dev workflows).
- **Release/DevOps Agent** - Helps with deployment scripts, CI/CD, and environment changes (in DevOps expansion packs).

## Documentation and Strategy Agents

- **Tech Writer / Documentarian** - Maintains project context, change logs, and technical docs.
- **Project Context Curator** - Generates and updates `project-context.md` from code and architecture.
- **Retrospective Facilitator** - Runs retrospectives and records lessons learned.
- **Researcher** - Supports deeper market and technical research beyond initial analysis.
- **Business Strategist** - Aligns features with business goals and roadmap (from strategy expansion packs).

## Creative and Auxiliary Agents

- **Idea Coach / Brainstorming Coach** - Runs guided brainstorming sessions for new products or features.
- **Quick-Spec Agent** - Creates concise tech specs for small changes (Quick Flow).
- **Quick-Dev Agent** - Implements ad-hoc changes directly from a quick spec.
- **Correct-Course Agent** - Handles major mid-sprint changes and replans stories.
- **Support / Help Agent** - Powers `/bmad-help`, teaching which workflow or agent to use next.
