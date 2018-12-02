import requests
from bs4 import BeautifulSoup

from func_stock_price import get_stock_price

from func_Arabian import get_Arabian
from func_Bloomberg import get_Bloomberg
from func_CNN import get_CNN
from func_Financialex import get_Financialex
from func_Fortune import get_Fortune
from func_Nasdaq import get_Nasdaq
from func_Yahoo import get_Yahoo


#AAPL_result.txt			func_CNN.py			func_Yahoo.py			list_of_web.ipynb
#CNN_selenium_scraping_yang.py	func_Eight_emotion.py		func_filter.py			main.py
#__pycache__			func_Financialex.py		func_pos_neg.py			module.txt
#func_Arabian.py			func_Fortune.py			func_stock_price.py
#func_Bloomberg.py		func_Nasdaq.py			func_word_cloud.py


class Company:

    """Results are all based on Yahoo Finance."""

    #import webscraping function in the same folder


    url_base = 'https://finance.yahoo.com/lookup?s='

    #constructor
    def __init__(self,keyword, email=False, warning=False):
        self.keyword = keyword
        self.ticker = self.ticker(keyword)
        self.email = email
        self.warning = warning

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
    
    @ticker.setter
    def ticker(self,keyword):
        t = self.ticker(keyword)
        self._ticker = t

#    @property
#    def monitor(self):
#        return self._monitor
#    
#    @monitor.setter
#    def monitor(self,x):
#        if x == True:
#            
#        self._monitor = x
#    
#    @property
#    def warning(self):
#        return self._warning
#    
#    @warning.setter
#    def warning(self,x):
#        if x == True:
#            
#        self._ticker = t
#
#    

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
        text_ = get_Yahoo(self.ticker, day=day, out_put=out_put)
        text_ = text_ + get_Arabian(self.keyword, day=day, out_put=out_put)
        text_ = text_ + get_Bloomberg(self.keyword, day=day, out_put=out_put)
        text_ = text_ + get_CNN(self.keyword, day=day, out_put=out_put)
        text_ = text_ + get_Financialex(self.keyword, day=day, out_put=out_put)
        text_ = text_ + get_Fortune(self.keyword, day=day, out_put=out_put)
        text_ = text_ + get_Nasdaq(self.ticker, day=day, out_put=out_put)
        return text_

    def price(self, day=7, plot=False):
        df =  get_stock_price(ticker=self.ticker, day=day)
        import pandas as pd
        import matplotlib.pyplot as plt
        if plot:
            df['Close'].plot()
            plt.savefig(f'{self.keyword}.png')
        return df


apple = Company('apple')
print(apple.news(20,True))
#apple.price(plot=True)

#print(apple.price(plot=True))
#apple.price(day=30,plot=True)
