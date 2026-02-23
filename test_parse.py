from bs4 import BeautifulSoup
import re

with open("satur_sample.html", "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

articles = soup.find_all("article", class_="row gx-0 py-4 group")
for article in articles:
    # Name
    name_el = article.find("a", class_="stretched-link")
    name = name_el.text.strip() if name_el else "N/A"
    
    # Stars
    stars = len(article.find_all("i", class_="icon-star"))
    
    # Price
    price_str = None
    for text in article.stripped_strings:
        if "€" in text and any(c.isdigit() for c in text):
            # Try to get the actual price which might be preceded by 'od' or 'zľava'
            price_str = text
            # Usually the price is in a strong or h3
    
    # Let's try finding the big price element
    price_element = article.select_one(".font-weight-bold.h3, .text-primary.h3, .h3")
    if price_element:
        price_str = price_element.text.strip()
        
    print(f"Hotel: {name} | Stars: {stars}* | Price: {price_str}")
    
    # Other details (Airport, Dates, Nights)
    # usually inside lists or spans
    details = article.find_all("li")
    for d in details:
         if "Nocí:" in d.text:
             print(" ", d.text.strip().replace("\n", " "))
         if "Odlet:" in d.text:
            print(" ", d.text.strip().replace("\n", " "))
         if "2026" in d.text or "2025" in d.text or "." in d.text:
            if "Termín:" in d.text or len(d.text) < 30:
                print(" ", d.text.strip().replace("\n", " "))
    print("-" * 40)
