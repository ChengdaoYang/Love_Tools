import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

def get_Yahoo(ticker, out_put=False):

    base_url = 'https://finance.yahoo.com'
    url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"

    response = requests.get(url)
    Soup = BeautifulSoup(response.content,'lxml')

    All_tags = Soup.find_all('a',
                            {'class':
                            'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)'
                            +'--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)'
                            +'--sm1024 Td(n) C(#0078ff):h C(#000)'})
    
    url_list = []
    for tag in All_tags:
        url_list.append(tag.get('href'))
    url_list   

    text = ''
    for url in url_list:
        response = requests.get(base_url + url)
        Soup = BeautifulSoup(response.content, 'lxml')
        All_tags = Soup.find_all('p', {'class':'canvas-atom canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm'})
    
        for tag in All_tags:
            text = text + (tag.get_text())

    if out_put:
        with open(f'{ticker}_result.txt', 'w') as fp:
            fp.write(text)

    return text


