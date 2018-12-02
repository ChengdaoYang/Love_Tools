import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import time
import random

def get_Yahoo(ticker,day=7, out_put=False, debug=False):
    #day is not yet functional, due to the difficulty in implimenting the yahoo webscraping
    base_url = 'https://finance.yahoo.com'
    url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"

    try:
        #request the url, Soup parse and get tag of each relavent article
        response = requests.get(url)
        if debug:
            print(response)

        if response.status_code == 200:
            if debug:
                print(response)
            Soup = BeautifulSoup(response.content,'lxml')
        else:
            return ''
        All_tags = Soup.find_all('a',
                                {'class':
                                'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)'
                                +'--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)'
                                +'--sm1024 Td(n) C(#0078ff):h C(#000)'})
        if debug:
            print(All_tags)

        #get all article links from a tags and put into a list
        url_list = []
        for tag in All_tags:
            if debug:
                print(tag.get('href'))
            url_list.append(tag.get('href'))


        if debug:
            print(url_list)
            print('start getting article from url_lists')
        #get text from each article url and put into one big lonf string
        text = ''
        
        for link in url_list:
            time.sleep(random.random())
            if debug:
                print(base_url + link)
            response = requests.get(base_url + link)
            Soup = BeautifulSoup(response.content, 'lxml')
            All_tags = Soup.find_all('p', {'class':'canvas-atom canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm'})
        
            if debug:
                print('getting text from:', base_url+link)
            for tag in All_tags:
                text = text + (tag.get_text())


    
        if out_put:
            with open(f'{ticker}_result.txt', 'w') as fp:
                fp.write(text)

        return text
    except:
        return ''

print(get_Yahoo('AAPL',out_put=True, debug=True))
