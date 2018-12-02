import requests
from bs4 import BeautifulSoup
import re
import datetime

def get_Nasdaq(name,day, out_put = False):
    text = "" 
    count = 1
    flag = True
    while (count <= 20 and flag):
        url = 'https://www.nasdaq.com/symbol/'+name+'/news-headlines?page=' + str(count)  
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print('can not connect',response.status_code)
                return None
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
                    if delta > day:
                        break       
                    link = container.a['href']
                    response = requests.get(link)
                    page = BeautifulSoup(response.content,'lxml')                     
                    paragraphs = page.find_all("p")                   
                    for paragraph in paragraphs:          
                        text += paragraph.text            
            count += 1   
            
            if out_put:
                with open(f'{name}_nasdaq.txt', 'w', encoding="utf-8") as fp:
                    fp.write(text) 
              
            return text   
        except:
            return None

print(get_Nasdaq('amzn',7,True))
                  
                
   