import datetime
import time
import requests
from bs4 import BeautifulSoup

from func_send_email import send_email
from func_stock_price import get_stock_price
from func_summary import get_summary

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
    def __init__(self,keyword, is_email=False):
        self.keyword = keyword
        self.ticker = self.ticker(keyword)
        self.is_email = is_email
        self.counter = datetime.timedelta(0)
        self.watch_it = None

    #getter & setter
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self,keyword):
        keyword = keyword[0].upper() + keyword[1:].lower()
        self._keyword = keyword

    @property
    def ticker(self):
        return self._ticker
    
    @ticker.setter
    def ticker(self,keyword):
        t = self.ticker(keyword)
        self._ticker = t

    @property
    def watch_it(self):
        return self._watch_it
    @watch_it.setter
    def watch_it(self, x):
        self._watch_it = x

            
    @property
    def counter(self):
        return self._counter
    @counter.setter
    def counter(self, x):
        self._counter = x        
 
    @property
    def elapsed(self):
        if self.watch_it:
            diff = (datetime.datetime.utcnow() - self.watch_it)
            time_elapsed = int(self.counter.total_seconds())+int(diff.total_seconds())
            if time_elapsed%2 == 0:
                print('send email')
            return time_elapsed
        return self.counter
    

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
        #text_ = text_ + get_Arabian(self.keyword, day=day, out_put=out_put)
        #text_ = text_ + get_Bloomberg(self.keyword, day=day, out_put=out_put)
        #text_ = text_ + get_CNN(self.keyword, day=day, out_put=out_put)
        #text_ = text_ + get_Financialex(self.keyword, day=day, out_put=out_put)
        #text_ = text_ + get_Fortune(self.keyword, day=day, out_put=out_put)
        #text_ = text_ + get_Nasdaq(self.ticker, day=day, out_put=out_put)
        return text_


    def price(self, day=7, plot=False):
        df =  get_stock_price(ticker=self.ticker, day=day)
        import pandas as pd
        import matplotlib.pyplot as plt
        if plot:
            df['Close'].plot()
            plt.show()
            plt.savefig(f'{self.ticker}_price.png')
            plt.close()
        return df
  

    def monitor(self):
        if self.watch_it:
            self.counter += (datetime.datetime.utcnow() - self.watch_it)
            self.watch_it = False
        else:
            self.watch_it = datetime.datetime.utcnow()
      

    def summary(self, day=7, lines=4, plot=False, save_plot=False, out_put=False):
        return get_summary(company=self, day=day, lines=lines, plot=plot, save_plot=save_plot, out_put=out_put)


    def email(self, email_list=['chengdaoyang@live.com','ms5705@columbia.edu']):
        send_email(company=self, email_list=email_list) 


    def __repr__(self):
        return "<{}: Clock {} ({})>".format(
            self.keyword,
            self.elapsed,
            'started' if self.watch_it else 'stopped' )






apple = Company('apple')

print(apple.keyword)
#print(apple.price())
#print(apple.summary())


#apple.email()
#print(apple.news(20,True))


#apple.price(plot=True)

#print(apple.price(plot=True))
#apple.price(day=30,plot=True)
#print(apple.elapsed)

apple.monitor()
print(apple)

time.sleep(2)
print(apple)
print(apple.elapsed)
time.sleep(1)
print(apple)

print(apple)
time.sleep(2)
print(apple)
apple.monitor()

