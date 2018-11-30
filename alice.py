# -*- coding: utf-8 -*-
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
#print(web1(stock_list))


name = 'sbux'
def webnasdaq(name):
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
