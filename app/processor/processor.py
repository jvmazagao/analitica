
import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup

from extractor.extractor import Extractor

class Processor:
    def get_data(self, ticker):
        url = f'https://www.fundamentus.com.br/detalhes.php?papel={ticker}'
        cookie_jar = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'),
                            ('Accept', 'text/html, text/plain, text/css, text/sgml, */*;q=0.01')]
        extractor = Extractor({})
        with opener.open(url) as link:
            content = link.read().decode('ISO-8859-1')
            soup = BeautifulSoup(content, 'html.parser')

            # Scraping all rows in the tables
            tables = soup.find_all('table', {'class': 'w728'})
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    cols = [col.text.strip() for col in cols]
                    if cols:  # If there are columns (non-empty row)
                        # cols = clean_cols(cols)
                        extractor.extract(cols)
        return extractor.data