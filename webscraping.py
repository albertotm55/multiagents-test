import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def scrape(self):
        html = self.fetch()
        soup = self.parse(html)
        return soup.prettify()

if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    scraper = WebScraper(url)
    print(scraper.scrape())