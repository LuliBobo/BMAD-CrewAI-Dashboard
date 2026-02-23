# Dokumentácia API pre Dashboard Backend

## 1. Názov a krátky popis 
Toto API poskytuje prístup k dôležitým backendovým metrikám pre Sales Dashboard, a to priamo z internej SQLite databázy. Je postavené vo frameworku Flask (Python). Umožňuje získať aktuálne štatistiky predajov, leadov, konverzií a aktívnych používateľov.

## 2. Ako otvoriť hotový `generated_backend.py`

1. **Inštalácia Flask:**
   Ak ešte nemáte Flask nainštalovaný, otvorte terminál a zadajte nasledujúci príkaz:
   ```bash
   pip3 install Flask
   ```

2. **Spustenie API:**
   Spusti server spustením súboru. V termináli napíšte:
   ```bash
   python3 generated_backend.py
   ```
   API naštartuje lokálny server. Bude dostupné cez webový prehliadač na adrese `http://127.0.0.1:5000/api/metrics`.

## 3. Architektúra prvkov (Návrh: Architect)

### Databázová schéma
Databáza pre Dashboard používa jednoduchý SQLite súbor aplikácie `sales_dashboard.db`. Obsahuje jednu tabuľku:

- **metrics**
  - `id`: Integer, Primárny kľúč, Autoincrement
  - `total_sales`: Real (Hodnota predajov)
  - `new_leads`: Integer (Počet leadov)
  - `conversion_rate`: Real (Miera konverzie)
  - `active_users`: Integer (Aktívni používatelia)

### Formát JSON a Endpointy
Aplikácia posúva dáta frontendu prostredníctvom HTTP GET payloadu z jedného hlavného koncového bodu:

- **Získanie aktuálnych metrík**
  - **Endpoint:** `/api/metrics`
  - **Metóda:** GET
  - **Odpoveď (Status 200 OK):**
    ```json
    {
      "active_users": 1200,
      "conversion_rate": 12.4,
      "new_leads": 342,
      "total_sales": 12450.0
    }
    ```

## Záver a zhodnotenie Code Reviewera
Vygenerovaný kód je čistý, logický a plne dodržuje navrhnutý systém model - databáza - endpoint od agenta `Architect`. Inicializácia pri inštancii zaručuje, že sa vytvorí schéma `metics` aj bez doterajšej prítomnosti `.db` súboru.
