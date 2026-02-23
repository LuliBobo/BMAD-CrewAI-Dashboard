# BMAD Help Playbook

Pouzi tento playbook pre konzistentne odpovede v style `/bmad-help`.

## 1. Rychle Mapovanie Intentu

| Help intent pouzivatela | Odporucany agent | Kedy delegovat na Orchestrator |
| --- | --- | --- |
| "Ktory agent mam pouzit?" | Orchestrator | Vzdy, ak request pokryva viac ako jednu fazu |
| "Neviem co dalej v projekte" | Support / Help Agent | Ak treba presny route medzi viacerymi rolnami |
| "Potrebujem PRD/priority" | Product Manager (PM) | Ak chyba kontext rozsahu a cielev |
| "Potrebujem architekturu/ADR" | Architect | Ak sa meni scope alebo non-functional poziadavky |
| "Potrebujem stories/sprint plan" | Scrum Master (SM) | Ak treba preplanuj sprint po zmene smeru |
| "Potrebujem implementovat zmenu" | Developer (Dev) | Ak je nejasna faza a treba najprv routovanie |
| "Potrebujem testy/QA" | QA / Quinn | Ak test scope zasahuje release rizika |
| "Potrebujem code review" | Code Reviewer | Ak sucasne treba refaktoring decision |
| "Potrebujem deploy/CI-CD" | Release/DevOps Agent | Ak sucasne treba zmenu architektury |
| "Potrebujem docs/changelog" | Tech Writer / Documentarian | Ak docs zavisia na zmene kontextu projektu |

## 2. Workflow Odporucania

- Discovery -> Planning: `Analyst -> Product Manager (PM) -> Architect -> Scrum Master (SM)`
- Build -> Quality: `Developer (Dev) -> QA / Quinn -> Code Reviewer -> Refactorer`
- Release -> Documentation: `Release/DevOps Agent -> Tech Writer / Documentarian -> Project Context Curator`
- Mid-sprint change: `Correct-Course Agent -> Scrum Master (SM) -> Developer (Dev)`

## 3. Sablony Odpovede

### A. Jednoducha help odpoved

```markdown
Odporucany Agent: <agent>
Preco:
- <jedna jasna veta>

Dalsi Krok:
- <jedna konkretna akcia>
```

### B. Nejasny alebo viacfazovy request

```markdown
Odporucany Agent: Orchestrator
Preco:
- Poziadavka zasahuje viac roli alebo faz.

Dalsi Krok:
- Spusti routovanie: python3 ../orchestrator/scripts/route_orchestrator.py --request "<text poziadavky>"
```

## 4. Gating Pravidla

- Nedavaj viac ako jedneho primarneho agenta.
- Pri neistote poloz max 2 upresnujuce otazky.
- Ak user pyta "ako pokracovat", konci odpoved konkretnym dalsim krokom.
- Ak user pyta "kto to ma urobit", najprv urci fazu (planovanie/build/QA/release/docs).
