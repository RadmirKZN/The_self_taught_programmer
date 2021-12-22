import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("a"):
            url = tag.get("href")
            x = open("../challenge_for module_1/challenge_parser/scrap_test_file_1.txt", "w")
            x.write("\n" + url)
            x.close()



news = "https://yandex.ru/news"
Scraper(news).scrape()
