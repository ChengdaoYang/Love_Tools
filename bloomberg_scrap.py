# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time



def web_bloomberg(name):
    dic = {}
    url = "https://www.bloombergquint.com/search?q=" + name
    response = requests.get(url)
    containers = BeautifulSoup(response.content,'lxml')
    
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