from bs4 import BeautifulSoup
import requests
import re

def scrape_satur_dubai():
    url = "https://www.satur.sk/last-minute/spojene-arabske-emiraty/dubaj"
    print(f"Sťahujem údaje zo stránky Satur: {url} ...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Chyba pri sťahovaní stránky.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="group")
    
    results = []
    
    for article in articles:
        name_el = article.find("a", class_="stretched-link")
        if not name_el:
            continue
            
        name = name_el.text.strip()
        
        # Filtrujeme len relevantné articles
        if not "Hotel" in name and not "Resort" in name and not "Villa" in name:
             if len(name) < 5:
                  continue
        
        stars = len(article.find_all("i", class_="icon-star"))
        
        price = 999999
        price_str = ""
        price_element = article.select_one(".font-weight-bold.h3, .text-primary.h3, .h3")
        if price_element:
            price_str = price_element.text.strip()
            # extract number
            nums = re.findall(r'\d+', price_str.replace(" ", ""))
            if nums:
                price = int(nums[0])
                
        details = article.find_all("li")
        nights = "N/A"
        airport = "N/A"
        dates = "N/A"
        
        for d in details:
            text = d.text.strip().replace("\n", " ").replace("  ", " ")
            if "Noc" in text:
                nights = text.split("Noc")[1].strip() if "Noc" in text else text
            elif "Odlet" in text:
                airport = text.split("Odlet:")[1].strip() if "Odlet:" in text else text
            elif "Termín" in text:
                dates = text.split("Termín:")[1].strip() if "Termín:" in text else text
            elif len(text) < 30 and ("2026" in text or "2025" in text or "." in text):
                pass # sometimes dates are just listed directly
                 
        results.append({
            "name": name,
            "stars": stars,
            "price": price,
            "price_str": price_str,
            "dates": dates,
            "nights": nights,
            "airport": airport
        })
        
    return results

def main():
    offers = scrape_satur_dubai()
    print(f"Celkovo nájdených všetkých ponúk na Satur.sk: {len(offers)}\n")
    
    for o in offers:
        print(f"🏨 Hotel: {o['name']} ({o['stars']}*)")
        print(f"💶 Cena na osobu: {o['price_str']}")
        print(f"📅 Termín: {o['dates']}")
        print(f"🌙 Počet nocí: {o['nights']}")
        print(f"✈️ Odletové letisko: {o['airport']}")
        print("-" * 50)
    
    print("\n" + "="*50)
    print("--- VYFILTROVANÉ VÝSLEDKY ---")
    print("Podmienky: <= 1200€ | >= 4* | Viedeň/Bratislava")
    print("="*50 + "\n")
    
    filtered = []
    for o in offers:
        if o['price'] <= 1200 and o['stars'] >= 4 and ("Viedeň" in o['airport'] or "Bratislava" in o['airport'] or o['airport'] == "N/A"):
            filtered.append(o)
            
    if not filtered:
         print("Bohužiaľ, nenašli sa žiadne ponuky spĺňajúce tieto prísne kritériá.")
    else:
        for f in filtered:
            print(f"🏨 Hotel: {f['name']} ({f['stars']}*)")
            print(f"💶 Cena na osobu: {f['price_str']}")
            print(f"📅 Termín: {f['dates']}")
            print(f"🌙 Počet nocí: {f['nights']}")
            print(f"✈️ Odletové letisko: {f['airport']}")
            print("-" * 50)

if __name__ == "__main__":
    main()
