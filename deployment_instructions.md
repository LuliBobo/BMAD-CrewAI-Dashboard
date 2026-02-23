# Návod na nasadenie do produkcie

Tento dokument bol generovaný pomocou BMAD DevOps Agenta. Všetko prebehlo automatizovane od kópera až po DevOps tím.

## Prečo sme použili Docker?
Docker je nástroj, ktorý umožňuje vytvárať a spravovať aplikácie v "kontajneroch". Kontajnery sú izolované prostredia, ktoré obsahujú všetko potrebné na spustenie aplikácie (samotný kód, Python, inštalačné balíky). To znamená, že náš Backend môže bežať na 100% zhodne na vašom Macu, ako aj niekde na produkčnom Ubuntu serveri v Cloude, bez závislosti od lokálneho prostredia. Pre náš Sales Dashboard sme použili Docker práve preto, aby sme zabezpečili bezbolestný *deployment*.

## Súbor `Dockerfile`
Tento súbor definuje inštrukcie na vytvorenie *Obrazu (Image)* kontajnera pre našu aplikáciu.

```dockerfile
# Použiť oficiálny Python obraz z Docker Hub
FROM python:3.9-slim

# Nastaviť pracovný adresár v kontajneri
WORKDIR /app

# Skopírovať súbor s požiadavkami do kontajnera na /app
COPY requirements.txt .

# Nainštalovať všetky závislosti špecifikované v requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Skopírovať zvyšok kódu aplikácie do kontajnera
COPY . .

# Nastaviť premennú prostredia pre Flask
ENV FLASK_APP=generated_backend.py

# Exponovať port, na ktorom aplikácia beží
EXPOSE 5000

# Príkaz na spustenie aplikácie
CMD ["flask", "run", "--host=0.0.0.0"]
```

## Súbor `docker-compose.yml`
Zatiaľ čo `Dockerfile` vytvorí obraz, tento súbor `docker-compose.yml` slúži na ľahšiu orchestráciu služby. Je to ten preferovaný spôsob, ako Docker kontajner reálne "nakopnúť".

```yaml
version: '3.8'

services:
  flask_app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
```

## Kroky na spustenie aplikácie
Aby ste spustili aplikáciu priamo na serveri s nainštalovaným Dockerom (napríklad DigitalOcean, AWS alebo u vás lokálne pred nasadením), otvorte terminál do tohto priečinka a vykonajte:

1. **Zostavte kontajner:**
   ```bash
   docker-compose build
   ```

2. **Spustite aplikáciu:**
   ```bash
   docker-compose up
   ```

Týmto spôsobom sa vaša aplikácia nainštaluje, stiahne balíček Python 3.9 do nezávislého pieskoviska (sandboxu) a zapne server, ktorý bude dostupný na adrese `http://localhost:5000`.
