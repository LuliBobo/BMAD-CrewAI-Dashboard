# Routovacia Mapa (21 Agentov)

Pouzi tuto mapu na vyber primarneho BMAD agenta podla zameru a fazy dorucovania.

## Trigger Matica

| Agent | Slovensky alias (JSON) | Smeruj ked poziadavka je hlavne o | Typicky vystup |
| --- | --- | --- | --- |
| Orchestrator | Koordinator | vyber spravneho workflowu alebo dalsieho agenta | routovacie rozhodnutie + handoff |
| Analyst | Analytik | zaramcovanie problemu, discovery, skory prieskum | analyza problemu, moznosti, draft briefu |
| Product Manager (PM) | Produktovy Manazer (PM) | rozsah PRD, potreby pouzivatelov, metriky uspechu | aktualizacie PRD, akceptacne kriteria |
| UX Designer | UX Dizajner | user flow, navrh interakcii, UX specifikacie | flow diagramy, UX specifikacia |
| Architect | Architekt | navrh systemu, ADR, technicke obmedzenia | navrh architektury, ADR |
| Scrum Master (SM) | Scrum Master (SM) | formovanie epikov/stories, sprint flow, sekvencovanie | epiky, stories, sprint plan |
| Developer (Dev) | Vyvojar (Dev) | implementacia stories a zmeny v kode | kod + testy |
| QA / Quinn | QA / Quinn | testovacia strategia, pokrytie automatizacie, udrzba testov | automatizovane testy, QA poznamky |
| Code Reviewer | Kontrolor Kodu | strukturovane review podla standardov a architektury | review findings a rizika |
| Refactorer | Refaktorer | citatelnost, udrziavatelnost, cielene vykonnostne zlepsenia | refactoring plan a patch |
| Release/DevOps Agent | Release/DevOps Agent | CI/CD, deploy skripty, zmeny prostredi | pipeline alebo deployment aktualizacie |
| Tech Writer / Documentarian | Technicky Pisatel / Dokumentarista | technicka dokumentacia, changelogy, usage poznamky | aktualizacie dokumentacie |
| Project Context Curator | Kurator Projektoveho Kontextu | udrzanie `project-context.md` v sulade s kodom | obnoveny projektovy kontext |
| Retrospective Facilitator | Facilitator Retrospektivy | reflexia po sprinte a zlepsenia | retrospektivny report |
| Researcher | Vyskumnik | hlbsi trhovy alebo technicky vyskum | syntetizovany vyskum |
| Business Strategist | Biznis Strateg | roadmapa/biznis alignment, prioritizacne dovody | strategicke odporucania |
| Idea Coach / Brainstorming Coach | Kouc Napadov / Brainstorming Kouc | vedena ideacia pre nove produkty/funkcie | sada napadov s hodnotiacimi kriteriami |
| Quick-Spec Agent | Quick-Spec Agent | mala zmena vo formate strucnej specifikacie | kratka implementacna specifikacia |
| Quick-Dev Agent | Quick-Dev Agent | rychla ad-hoc implementacia z malej specifikacie | mala kodova zmena |
| Correct-Course Agent | Agent Korekcie Smeru | zmena smeru pocas sprintu a replanning | revidovany plan a upravy stories |
| Support / Help Agent | Podpora / Help Agent | BMAD help prikazy a workflow guidance | odpoved pomoci s odporucanou cestou |

## Pravidla Pri Remize

1. Uprednostni vlastnictvo fazy pred vlastnictvom artefaktu.
2. Ak je poziadavka rozdelena medzi planovanie a build, smeruj najprv do planovania.
3. Ak pouzivatel chce okamzite kodovanie, smeruj na Developer (Dev), pokial riziko nevyzaduje Architect alebo PM najprv.
4. Ak sa pyta "ktory agent/workflow", smeruj na Orchestrator alebo Support / Help Agent.
5. Ak je istota nizka, smeruj na Analyst a poloz cielene upresnujuce otazky.

## Ocekavania Na Handoff

- Uved jedneho primarneho agenta a maximalne jedneho podporneho agenta.
- Zahrn ciel, potrebne vstupy, obmedzenia a kriterium hotovo.
- Prvy krok nech je konkretny a okamzite vykonatelny.
