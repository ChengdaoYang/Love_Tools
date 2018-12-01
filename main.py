import requests
from bs4 import BeautifulSoup

class Company:

    """Results are all based on Yahoo Finance."""

    url_base = 'https://finance.yahoo.com/lookup?s='

    def __init__(self,keyword):
        self.keyword = keyword
        self.ticker = self.ticker(keyword)

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self,keyword):
        self._keyword = keyword

    @property
    def ticker(self):
        return self._ticker
    #
    @ticker.setter
    def ticker(self,keyword):
        t = self.ticker(keyword)
        self._ticker = t

    def ticker(self,keyword):
        response = requests.get(self.url_base + keyword)
        results_pages = BeautifulSoup(response.content)
        all_aim_td_tags = results_pages.find_all('td',{'class':'data-col0 Ta(start) Pstart(6px) Pend(15px)'})
        if all_aim_td_tags == []:
            raise ValueError('No ticker found.')

        return all_aim_td_tags[0].find('a').text
