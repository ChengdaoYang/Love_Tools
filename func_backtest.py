
from func_signal import get_signal 
from func_filter import get_filtered

import datetime
from pandas_datareader import data as web

def get_backtest(ticker, day):
    
    from bs4 import BeautifulSoup
    import re
    import requests
    
    # input company name, backtest period
    # Output dictionary
    def get_daily_news(name, day, out_put = False):
    #    name = 'aapl'
        count = 1
        dic = {}
        text = ""
        last_publish_date = datetime.datetime.today()
        flag = True
    
        while (count <= 100 and flag == True):
            url = 'https://www.nasdaq.com/symbol/'+ name + '/news-headlines?page=' + str(count)  
            response = requests.get(url)
            containers = BeautifulSoup(response.content,'lxml')      
            containers_news = containers.find("div",{"class":"news-headlines"})
            if containers_news == None:
                return dic
    
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
                            text = text + " " + paragraph.text
            count += 1
        return dic
    
    def get_weekly(ticker, start):
        
    #    start = datetime.datetime(2018, 11, 26, 0, 0)
        end = start + datetime.timedelta(7)
        df = web.DataReader(ticker, 'yahoo', start, end)['Adj Close']
        
        ratio = df[-1]/df[0] 
        if ratio > 1.002:
            tag = 1
        elif ratio < 1/1.002:
            tag = -1
        else:
            tag = 0
        return tag
    
    dic = get_daily_news(ticker, day, out_put = False)
    
    output = []
    for date_ in dic.keys():
        text = dic[date_]
        text = get_filtered(ticker, text, out_put = False)
        # predict
        predict = get_signal(text, threshold = 1.5)
        # reality
        real = get_weekly(ticker, date_)
        output.append(str(date_),predict,real)
        
    return output
#get_backtest('aapl', 7)
        

