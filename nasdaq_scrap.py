# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import re
import datetime


#name = 'sbux'
def web_nasdaq(name):
    dic = {}
    text = "" 
    count = 1
    flag = True
    while (count <= 20 and flag):
        url = 'https://www.nasdaq.com/symbol/'+name+'/news-headlines?page=' + str(count)        
        response = requests.get(url)
        containers = BeautifulSoup(response.content,'lxml')      
        containers_news = containers.find("div",{"class":"news-headlines"})
        for container in containers_news.find_all("div"):
            if container.small is not None:
                t = str(container.small)
                pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
                match = re.findall(pattern,t)
                if match == []:
                    continue
                public_date = datetime.datetime.strptime(match[0], '%m/%d/%Y')
                today = datetime.datetime.today()
                delta = (today - public_date).days
                if delta > 31:
                    flag = False
                    break       
                response = requests.get(link)
                page = BeautifulSoup(response.content,'lxml')                     
                paragraphs = page.find_all("p")                   
                for paragraph in paragraphs:          
                    text += paragraph.text            
        count += 1                        
        dic[name] = text       
    return dic    
#webnasdaq(name)
                  
                
   