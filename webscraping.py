import requests
from bs4 import BeautifulSoup

def webscrape_bank(bank_url):
    response = requests.get(bank_url)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error al acceder a la página'

if __name__ == '__main__':
    bbva_url = 'https://www.bbva.es/'
    sabadell_url = 'https://www.bancsabadell.com/'
    bbva_content = webscrape_bank(bbva_url)
    sabadell_content = webscrape_bank(sabadell_url)
    print('Contenido de BBVA:', bbva_content)
    print('Contenido de Sabadell:', sabadell_content)