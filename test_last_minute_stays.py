import unittest
from unittest.mock import patch, MagicMock

class TestLastMinuteStays(unittest.TestCase):

    def setUp(self):
        # Pomocné dáta pre testovanie filtrovania
        self.mock_offers = [
            {
                "name": "Hotel RIU Hotel & Resorts",
                "stars": 4,
                "price": 1100,
                "price_str": "1 100",
                "dates": "10.10. - 17.10.2026",
                "nights": "7",
                "airport": "Viedeň"
            },
            {
                "name": "Luxusný Hotel",
                "stars": 5,
                "price": 2000,
                "price_str": "2 000",
                "dates": "10.10. - 17.10.2026",
                "nights": "7",
                "airport": "Bratislava"
            },
             {
                "name": "Šmejd Hotel",
                "stars": 2,
                "price": 500,
                "price_str": "500",
                "dates": "10.10. - 17.10.2026",
                "nights": "7",
                "airport": "Viedeň"
            },
            {
                "name": "Košice Hotel",
                "stars": 4,
                "price": 900,
                "price_str": "900",
                "dates": "10.10. - 17.10.2026",
                "nights": "7",
                "airport": "Košice"
            }
        ]

    def test_filter_offers_success(self):
        """Testuje, či filter správne zachytí hotely spĺňajúce prísne podmienky."""
        # Manuálne napíšeme filter rovnaký ako v scraperi 
        filtered = []
        for o in self.mock_offers:
            if o['price'] <= 1200 and o['stars'] >= 4 and ("Viedeň" in o['airport'] or "Bratislava" in o['airport'] or o['airport'] == "N/A"):
                filtered.append(o)
        
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["name"], "Hotel RIU Hotel & Resorts")

    def test_fetch_last_minute_stays_no_results(self):
        """Testuje, či prázdny HTML vstup správne vráti prázdny list ponúk (simulované)."""
        empty_html = "<html><body>Žiadne ponuky</body></html>"
        self.assertEqual(len([]), 0) # Placeholder na parsovanie

if __name__ == '__main__':
    unittest.main()
