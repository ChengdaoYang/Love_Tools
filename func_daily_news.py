import requests
from bs4 import BeautifulSoup
import re
import datetime

def get_daily_news(name, day, out_put = False):
    name = 'aapl'
    count = 1
    dic = {}
    a ={}
    text = ""
    last_publish_date = datetime.datetime.today()
    flag = True
    while (count <= 100 and flag == True):
        url = 'https://www.nasdaq.com/symbol/'+ name + '/news-headlines?page=' + str(count)  
        response = requests.get(url)
        containers = BeautifulSoup(response.content,'lxml')      
        containers_news = containers.find("div",{"class":"news-headlines"})

        for container in containers_news.find_all("div"):
            if container.small is not None and container.a['target'] != "_blank":
                t = str(container.small)
                pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
                match = re.findall(pattern,t)
                if match != []:
                    publish_date = datetime.datetime.strptime(match[0], '%m/%d/%Y')
                    today = datetime.datetime.today()
                    delta = (today - publish_date).days
                    if delta > day:
                        flag = False
                        break 
                    print(publish_date, last_publish_date)
                    if publish_date.weekday() > last_publish_date.weekday() or (last_publish_date - publish_date).days > 7:
#                         print('next')
                        dic[last_publish_date] = text
                        if out_put:
                            with open(f'{name}_nasdaq.txt', 'a', encoding="utf-8") as fp:
                                fp.write(str(last_publish_date)+ '\n' + text) 
                        text = ""

                    last_publish_date = publish_date  
                    link = container.a['href']
#                     print(link)
#                     a[link] = text
                    response = requests.get(link)                       
                    page = BeautifulSoup(response.content,'lxml')                     
                    paragraphs = page.find_all("p")                   
                    for paragraph in paragraphs:          
                        text += paragraph.text
        count += 1

    return dic