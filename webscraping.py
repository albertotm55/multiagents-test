# webscraping.py

import requests
from bs4 import BeautifulSoup

# Función para realizar web scraping

def webscrape(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

# Ejemplo de uso
url = 'https://example.com'
scraped_data = webscrape(url)
print(scraped_data)