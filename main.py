import datetime
import time
import requests
from bs4 import BeautifulSoup

#import class method in the same folder
from func_send_email import creepy_team
from func_send_email import send_email
from func_stock_price import get_stock_price
from func_summary import get_summary
from func_signal import get_signal
from func_backtest import get_backtest

#import web scraping function inwith the saem directory
from func_Arabian import get_Arabian
from func_Bloomberg import get_Bloomberg
from func_CNN import get_CNN
from func_Financialex import get_Financialex
from func_Fortune import get_Fortune
from func_Nasdaq import get_Nasdaq
from func_Yahoo import get_Yahoo



class Company:
    '''Company object will help you do financial analyse, if you have internet'''

    #user_email:  (single user for now)
    email_list = [input('please type your email address, to recieve notification of monitoring stocks\n').strip()]

    #constructor
    def __init__(self,keyword, is_email=False, day=7, interval=2):
        self.keyword = keyword
        self.ticker = self.ticker(keyword)
        self.counter = datetime.timedelta(0)
        self.day = day
        #interval is seconds,  use math to convert it to hours below
        self.interval = int(interval*2)
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
    def day(self):
        return self._day

    @day.setter
    def day(self,x):
        if x <= 0:
            raise ValueError('day must be positive, bro!')
        self._day = x


    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, x):
        if x < 0:
            raise ValueError('interval cannot be negative')
        self._interval = x
            

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
            if time_elapsed%self.interval == 0:
                self.email()
                print('send email')
            return time_elapsed
        return self.counter
    

    #class methods:
    #Ticker function will get the ticker from Yahoo base on company name
    def ticker(self,keyword):
        url_base = 'https://finance.yahoo.com/lookup?s='
        response = requests.get(url_base + keyword)
        results_pages = BeautifulSoup(response.content)
        all_aim_td_tags = results_pages.find_all('td',{'class':'data-col0 Ta(start) Pstart(6px) Pend(15px)'})
        if all_aim_td_tags == []:
            raise ValueError('No ticker found.')

        return all_aim_td_tags[0].find('a').text

    
    #News function get all news article from Yahoo, CNN ,Fortune, Bloomber.. and return a long str contains all.
    def news(self, out_put=False):
        print('getting news form Yahoo...')
        text_ = ''
        text_ = get_Yahoo(self.ticker, day=self.day, out_put=out_put)
        print('getting news from Arbian...')
        #text_ = text_ + get_Arabian(self.keyword, day=self.day, out_put=out_put)
        print('getting news from Bloomberg...')
        #text_ = text_ + get_Bloomberg(self.keyword, day=self.day, out_put=out_put)
        print('getting news from CNN...')
        #text_ = text_ + get_CNN(self.keyword, day=self.day, out_put=out_put)
        print('getting news from Financialex...')
        #text_ = text_ + get_Financialex(self.keyword, day=self.day, out_put=out_put)
        print('getting news from Fortune...')
        #text_ = text_ + get_Fortune(self.keyword, day=self.day, out_put=out_put)
        print('getting news from Nasdaq...')
        #text_ = text_ + get_Nasdaq(self.ticker, day=self.day, out_put=out_put)
        return text_


    #price method will read Company's stock price return a pandas'Dataframe of it price
    def price(self, plot=False, save_plot=False):
        df =  get_stock_price(ticker=self.ticker, day=self.day)
        import pandas as pd
        import matplotlib.pyplot as plt
        if plot:
            fig = plt.figure()
            df['Close'].plot()
            plt.draw()
            plt.pause(5)
         
        if save_plot:
            plt.ioff()
            fig = plt.figure()
            df['Close'].plot()
            plt.savefig(f'{self.ticker}_price.png')
            plt.close(fig)
        return df
  

    #this awsome function will monitor the Company() and send your emails of its news summary, price, the prediction, base on the preset interval
    def monitor(self):
        if self.watch_it:
            self.counter += (datetime.datetime.utcnow() - self.watch_it)
            self.watch_it = False
        else:
            self.watch_it = datetime.datetime.utcnow()

      

    def summary(self, lines=4, plot=False, save_plot=False, out_put=False):
        return get_summary(company=self, day=self.day, lines=lines, plot=plot, save_plot=save_plot, out_put=out_put)


    #email function, wehn call, will send a email about summary, prediction adn price w/s pic to you instantly
    def email(self):
        email_l = self.email_list
        email_l.extend(creepy_team())
        send_email(company=self, email_list=email_l) 

    #this function will predict the stock price base on news it reads online
    def prediction(self):
        result = get_signal(text=self.news())
        return result

    #will backtest the Company's prediction accuracy base on old data/news, with option to out_put plot and show plot
    def backtest(self, plot=False, save_plot=False):
        try:
            import matplotlib.pyplot as plt
            list_ = get_backtest(ticker = self.ticker, day = 30)
            date_list = []
            num_list = []
            for i in list_:
                date_list.append(i[0])
                try:
                    num_list.append(i[1] & i[2])
                except:
                    return None
            if plot:
               plt.bar(range(len(num_list)), num_list, color='red', tick_label=date_list)
               plt.show()


            if save_plot:
                plt.ioff()
                fig = plt.figure()
                plt.bar(range(len(num_list)), num_list, color='red', tick_label=date_list)
                plt.show()
                plt.savefig(f'{self.ticker}_backtest.png')
                plt.close(fig)
            pass
        except:
            print('no available data for plot backtesting')
            return None

    def __repr__(self):
        return "<{}: $ {} time:{}seconds, monitor:{}>".format(
            self.keyword,
            self.price()['Close'].iloc[0],
            (self.elapsed),
            'started' if self.watch_it else 'stopped' )


