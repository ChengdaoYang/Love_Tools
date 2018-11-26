# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:45:12 2018

@author: xws
"""
import requests
#import re
from bs4 import BeautifulSoup
import time

#stock_list = ["Apple", "Google", "Microsoft", "Facebook", "Cisco", "Amazon"]
stock_list = ["Apple"]
def web1(stock_list):
    dic = {}
    for name in stock_list:
        url = "https://www.bloombergquint.com/search?q=" + name
        response = requests.get(url)
        containers = BeautifulSoup(response.content,'lxml')
        
#        data = []
        text = ""
        for container in containers.find_all("li",{"class":"topic-page__item"}):
#            title = container.h3.a.text
            link = "https://www.bloombergquint.com" + container.h3.a["href"]
            t = container.time["datetime"]
            delta = round((time.time() - float(t[:-3]))/86400,2)
            if delta > 31:
                break
            
            response = requests.get(link)
            page = BeautifulSoup(response.content,'lxml')
            paragraphs = page.find_all("p")
#            text = ""
            for paragraph in paragraphs:
                text += paragraph.text
#            data.append((title,link,delta,text))
            
        dic[name] = text    
        
    return dic
print(web1(stock_list))
