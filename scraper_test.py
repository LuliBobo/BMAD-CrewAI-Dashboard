from playwright.sync_api import sync_playwright
import time

def fetch_rendered_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        
        # SATUR
        print("Fetching Satur...")
        page.goto("https://www.satur.sk/last-minute/spojene-arabske-emiraty/dubaj", timeout=60000)
        time.sleep(5)
        with open("satur_rendered.html", "w") as f:
            f.write(page.content())
            
        # KARTAGO
        print("Fetching Kartago...")
        page.goto("https://www.kartago.sk/vysledky-vyhladavania?d=64087%7C64094%7C64089%7C64090%7C64091%7C64095%7C64086%7C64092%7C64096%7C64093&dd=2026-02-20&nn=7%7C8%7C9%7C10%7C11%7C12%7C13%7C14&rd=2026-04-22&to=483%7C1837%7C3437%7C3789&tt=1", timeout=60000)
        time.sleep(5)
        with open("kartago_rendered.html", "w") as f:
            f.write(page.content())
            
        browser.close()

if __name__ == "__main__":
    fetch_rendered_html()
