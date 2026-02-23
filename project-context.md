# Kontext Projektu: Ukážka metódy BMAD

Tento súbor slúži ako centrálny bod uchovávajúci technický a biznisový kontext nášho "Full-Stack AI Team" experimentu s rámcom CrewAI na používateľovom stroji.

## Architektúra a Agenti
Základný projekt `bmad_crewai_example.py` úspešne beží so súborom **7 špecialistov**:
1.  **Orchestrator**: Rozdeľuje úlohy (Process.sequential).
2.  **Analyst**: Vytvára požiadavky (Product Briefs).
3.  **UX Designer**: Definuje vizuálny štýl (Téma, Grid, Farby).
4.  **Developer**: Kódi výsledný HTML/CSS dokument.
5.  **QA (Quinn)**: Overuje sémantiku a uzatvorenie `<style>` HTML tagov.
6.  **Code Reviewer**: Zabezpečuje použitie dizajnových vzorov (Design Patterns, Semantic HTML).
7.  **Tech Writer**: Definuje kontext a štýlom typickým komunitných sprievodcov píše finálnu `README` (.md) dokumentáciu k novovytvorenému kódu.

## Technické obmedzenia a zistenia (Dôležité!)
- Prostredie macOS beží na verzii Pythonu **3.9.6**.
- Najnovšie verzie rámca CrewAI (napríklad verzia > `0.28.8`) nie sú na 100% zlučiteľné so syntaxou Python 3.9 (používajú notácie ako `type | None`).
- Kvôli zachovaniu stability sa celý projekt pre CrewAI udržiava na knižniciach starších `pydantic` vydaní a `crewai==0.1.32`.
- Knižnice vydávajú "Deprecation" varovania, ktoré sú účelovo stlmené v záhlaví súboru kvôli čistejšiemu výstupu konzoly počas Crew execution.
- Framework neprihladá veľkú prekážku lokálnemu behu, avšak Orchestrátori lepšie zohrávajú svoje roly s modernými API-Models od dodávateľov (napríklad používaním modelu `gpt-4o-mini`).

## Histórie a Úspechy implementácie
- **V1: Dubai Travel Bot** - Agenti s pomocou BeautifulSoup scrapovali a filtrovali hotely odletov.
- **V2: Webový Dashboard** - Pridaný `UX Designer` a prepracovaný `user_request` úspešne zmenil celú líniu tímu na vydanie elegantného UI komponentu. (Aktuálna verzia skriptu).
