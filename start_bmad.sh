#!/bin/bash

# ==========================================
# BMAD 21 Agents - Vstupné Produkčné Rozhranie
# ==========================================
# Tento skript slúži na bezpečné a spoľahlivé naštartovanie
# vášho UI a API backendu na produkčnom WSGI servri (Gunicorn).

echo "🛡️ Spúšťam BMAD Command Center..."

# Nastavenie ciest
export FLASK_APP=generated_backend.py
export FLASK_ENV=production

# Kontrola spustenia vo vnútri priečinka
if [ ! -f "generated_backend.py" ]; then
    echo "❌ Chyba: Spúšťate skript zo zlého priečinka. Prosím, prisuňte sa do /Users/macbookprosukromne/Documents/BMAD."
    exit 1
fi

# Spustenie WSGI Servera Gunicorn so 4 workermi
# Bindujeme ho na lokálny port 5000 (rovnako ako predtým vývojový Flask)
gunicorn -w 4 -b 127.0.0.1:5000 generated_backend:app

# (Ak nemáte gunicorn, automaticky skript vypíše chybu, v tom prípade spustite 'pip install gunicorn')
