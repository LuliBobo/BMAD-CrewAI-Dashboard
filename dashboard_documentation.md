# Dokumentácia pre nový Dashboard

## 1. Názov a krátky popis vzhľadu Dashboardu
Názov: **Moderný Dashboard**  
Popis: Tento Dashboard je navrhnutý s dôrazom na moderný vzhľad a používateľskú prívetivosť. Používa svieže farby, prehľadné rozloženie a responzívny dizajn, ktorý sa prispôsobuje rôznym zariadeniam. Vizuálna téma je minimalistická, pričom kladie dôraz na jednoduché a intuitívne ovládanie.

## 2. Ako otvoriť hotový `generated_dashboard.html`
Aby ste mohli zobraziť hotový Dashboard, postupujte podľa týchto krokov:
1. Otvorte súborový prehliadač vo svojom počítači.
2. Prejdite do priečinka, kde sa nachádza súbor `generated_dashboard.html`.
3. Dvojitým kliknutím na súbor ho otvoríte vo vašom predvolenom webovom prehliadači.
4. Teraz by ste mali vidieť Dashboard vo formáte HTML.

## 3. Architektúra prvkov
Dashboard obsahuje nasledujúce kľúčové metriky a prvky:
- Celkové predaje: $12,450
- Počet nových Leadov: 342
- Konverzný pomer: 12.4%
- Aktívni používatelia: 1,200

### Štylizácia (UX Designer Patterns)
Prvky Dashboardu boli štýlované pomocou moderných CSS techník, vrátane:
- **Flexbox a Grid**: Tieto techniky (2 stĺpce, 2 riadky) zabezpečujú flexibilné a responzívne rozloženie, ktoré sa prispôsobuje rôznym veľkostiam obrazoviek.
- **Farby a písma**: Background má farbu `#f4f7f6`. Karty sú `#FFFFFF` a používajú font `Roboto`. Text má `#333333` a subtext `#777777`.
- **Tieňovanie kariet**: Implementovaný moderný flat shadow (box-shadow).

### Pripomienky k implementácii od QA Agenta a Code Reviewera
- **Dostupnosť**: Je potrebné pridať ARIA atribúty a `alt` texty.
- **Tlačidlá**: HTML tag tlačidla Refresh neslúži ako funkčný submit na odoslanie formulára (zatiaľ ide len o UI placeholder).
