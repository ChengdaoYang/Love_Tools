import requests
from bs4 import BeautifulSoup
from func_Yahoo import get_Yahoo
from func_stock_price import get_stock_price


class Company:

    """Results are all based on Yahoo Finance."""

    #import webscraping function in the same folder


    url_base = 'https://finance.yahoo.com/lookup?s='

    #constructor
    def __init__(self,keyword):
        self.keyword = keyword
        self.ticker = self.ticker(keyword)


    #getter & setter
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

    #class methods:

    #Ticker function will get the ticker from Yahoo base on company name
    def ticker(self,keyword):
        response = requests.get(self.url_base + keyword)
        results_pages = BeautifulSoup(response.content)
        all_aim_td_tags = results_pages.find_all('td',{'class':'data-col0 Ta(start) Pstart(6px) Pend(15px)'})
        if all_aim_td_tags == []:
            raise ValueError('No ticker found.')

        return all_aim_td_tags[0].find('a').text

    
    #News function get all news article from Yahoo, CNN ,Fortune, Bloomber.. and return a long str contains all.
    def news(self, day=7, out_put=False):
        text_ = ''
        text_ = get_Yahoo(self.ticker)
#        text_ = text_ + get_         
#        text_ = text_ + get_
#        text_ = text_ + get_
#        text_ = text_ + get_
#        text_ = text_ + get_
#        text_ = text_ + get_
#        text_ = text_ + get_
        return text_

    def price(self, day=7, plot=False):
        df =  get_stock_price(ticker=self.ticker, day=day)
        import pandas as pd
        import matplotlib.pyplot as plt
        if plot:
            df['Close'].plot()
            plt.show()
        return df

apple = Company('apple')
print(apple.price(plot=True))

