web_list = [(0, 'CNN Money', 'http://money.cnn.com/'),
 (4, 'Yahoo ', 'https://finance.yahoo.com/'),
 (8, 'Music Business Worldwide', 'https://www.musicbusinessworldwide.com/'),
 (12, 'LiveMint', 'http://www.livemint.com/'),
 (16, 'Business Today ', 'http://www.businesstoday.in/'),
 (20, 'Moneyweb ', 'https://www.moneyweb.co.za/'),
 (24, 'Zee Business', 'http://www.zeebiz.com/'),
 (28, 'BNamericas', 'https://www.bnamericas.com/'),
 (32, 'Baystreet', 'http://www.baystreet.ca/'),
 (36, 'Business Matters ', 'http://www.bmmagazine.co.uk/'),
 (40, 'Long Island Business News', 'http://libn.com/'),
 (44, 'Thailand Business News', 'https://www.thailand-business-news.com/')]

import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

#fail to scrap CNN becasue it use javascript
#def get_article_CNN(name):
#    
#    url = f"https://www.cnn.com/search/?size=10&q={name}&category=business"
#    respones = requests.get(url)
#    Soup = BeautifulSoup(respones.content.decode('utf-8'))
#    All_tags = Soup.find_all('h3')
#    for tag in All_tags:
#        #A_tag = tag.find('a')
#        print(tag)
#        #pirnt(A_tag.get('href'))
#    
#

#get_article_CNN('apple')

#yahoo
ticker = "AAPL"
url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"
response = requests.get(url)
print(response)
Soup = BeautifulSoup(response.content,'lxml')
All_tags = Soup.find_all('a',{'class':'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)'})

base_url = 'https://finance.yahoo.com'
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
#         print(tag.get_text())
        text = text + (tag.get_text())
print('text')
