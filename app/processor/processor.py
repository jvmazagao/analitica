
import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup

class Processor:
    def clean_key(self,key):
        return key.lstrip('?')

    def parse_data(self, data: dict, elements):
        if len(elements) == 1:
            key = self.clean_key(elements.pop())
            data[key] = {}
            return data

        if len(elements) == 2:
                key_1, key_2 = [self.clean_key(x) for x in elements]
                if key_1 == 'Últimos 12 meses':
                    data['Dados demonstrativos de resultados'][key_1] = {}
                    data['Dados demonstrativos de resultados'][key_2] = {}
                else: 
                    data[key_1] = {}
                    data[key_2] = {}
                return data

        if len(elements) == 4:
            for i in range(0, 4, 2):
                key, value = self.clean_key(elements[i]), elements[i+1]
                if 'Dados demonstrativos de resultados' in data:
                    if i == 0:
                        data['Dados demonstrativos de resultados']['Últimos 12 meses'][key] = value
                    else: 
                        data['Dados demonstrativos de resultados']['Últimos 3 meses'][key] = value
                if 'Dados Balanço Patrimonial' in data:
                    data['Dados Balanço Patrimonial'][key] = value
                else:
                    data[key] = value
        
        if len(elements) == 6:
            for i in range(0, 6, 2):
                key, value = self.clean_key(elements[i]), elements[i+1]
                if i == 0:
                    data['Oscilações'][key] = value
                else:
                    data['Indicadores fundamentalistas'][key] = value


        return data

    def get_data(self, ticker):
        url = f'https://www.fundamentus.com.br/detalhes.php?papel={ticker}'
        cookie_jar = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'),
                            ('Accept', 'text/html, text/plain, text/css, text/sgml, */*;q=0.01')]
        data = {}
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
                        data = self.parse_data(data, cols)
        return data