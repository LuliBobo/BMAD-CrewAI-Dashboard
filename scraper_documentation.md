# Názov
Testovanie skriptu pre vyhľadávanie posledných minútových pobytov

## Krátky popis
Tento skript je určený na automatizované testovanie funkčnosti vyhľadávania posledných minútových pobytov na stránkach Satur.sk a Kartago.sk pre destináciu Dubaj. Využíva knižnicu `unittest` na vytváranie a vykonávanie testov, pričom sa zabezpečuje, aby výstupy zodpovedali očakávaným výsledkom bez reálnych HTTP požiadaviek cez mockovanie.

## Požiadavky na prostredie
Pre spustenie skriptu sú potrebné nasledujúce knižnice:
- `requests`
- `unittest`
- `beautifulsoup4`

Na inštaláciu potrebných knižníc použite nasledujúci príkaz:
```bash
pip install requests beautifulsoup4
```

## Návod na spustenie
Skript môžete spustiť priamo z príkazového riadku. Uistite sa, že máte nainštalované všetky potrebné knižnice. Potom vykonajte nasledujúci príkaz:
```bash
python test_last_minute_stays.py
```
Tento príkaz spustí všetky definované testy od QA agenta v súbore `test_last_minute_stays.py`.

## Architektúra riešenia
Skript obsahuje nasledujúce funkcie a triedy:

### 1. scraper_dubai.py (Skript od Vývojára)
*   `get_html(url)`: Sťahuje stránku cez HTTP requests.
*   `parse_offers(html_content, source)`: Číta HTML strom a extrahuje hotel, počet hviezdičiek, cenu a odletové letisko.
*   `filter_offers(offers)`: Odstraňuje hotely, ktoré nespĺňajú podmienky 1200€ a aspoň 4*.
*   `print_offers(offers)`: Výpis výsledkov.

### Trieda: `TestLastMinuteStays` (Skript od QA agenta)
Toto je hlavná trieda, ktorá obsahuje testy pre funkcie vyhľadávania pobytov.

#### Metódy:
- `test_fetch_last_minute_stays(self, mock_get)`
  - **Popis:** Testuje, či funkcia na získavanie posledných minútových pobytov vracia zoznam pobytov s mocknutým requests callom.
  
- `test_fetch_last_minute_stays_no_results(self, mock_get)`
  - **Popis:** Testuje, či funkcia správne zvláda situáciu, keď nie sú k dispozícii žiadne pobyty.

Skript obsahuje aj dôvody na použitie mockovania pre HTTP požiadavky a používanie konštánt pre očakávané hodnoty, čo zvyšuje čitateľnosť a údržbu kódu.

---
*Vygenerované agentom BMAD: Tech Writer (Technický spisovateľ)*
