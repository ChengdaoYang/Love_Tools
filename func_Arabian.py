# https://www.arabianbusiness.com/
# input: company name, timedelta, out_put(determine whether to write the text to a file)

import requests
from bs4 import BeautifulSoup
import datetime

def get_Arabian(name, day, out_put=False):
    
    #for l in lists:
    url_21 = 'https://www.arabianbusiness.com/search?q=' + name + '&sort=date'
    try:
        response_21 = requests.get(url_21)
        if response_21.status_code != 200:
            return ''

        result_page_21 = BeautifulSoup(response_21.content, 'lxml')
        article_tags_21 = result_page_21.find_all('h3', class_='g-tit')
        text = ''
        for tag in article_tags_21:
        #    title = tag.text.strip()
            link1 = tag.a['href']
            link = 'https://www.arabianbusiness.com' + link1

            response_tag = requests.get(link)
            try: 
                if response_tag.status_code != 200:
                    return ''
            
                result_page = BeautifulSoup(response_tag.content, 'lxml')
                date = result_page.find_all('div',class_= 'date')
                d = str(date)
                dd = d[23:34].replace(" ",'')
                if dd == '':   # filter the pages without a date
                    pass
                else:
                    date1 =datetime.datetime.strptime(dd,'%d%b%Y')
                    #print(date1)
                    t1 = datetime.datetime.now() - date1
                    t2 = t1.days
                    if t2 > day:
                        pass
                    else:
                        paras = result_page.find_all("p")
                        for para in paras:
                            text  = text + ' ' + para.text
            except: 
                continue
        if out_put:
            with open(f'{name}_AB_news.txt', 'w') as fp:
                fp.write(text)
        return text
    
    except:
        return '' 


#print(get_Arabian('Apple',day=7))
