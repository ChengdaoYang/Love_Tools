#author: ms5705 
#website: http://www.financialexpress.com/
#stocks: anything in a list

import requests
from bs4 import BeautifulSoup
from datetime import datetime

lists = ['apple', 'starbucks']


def website2(my_list):
    web2 = {}
    for l in lists:
        print(l)
        url_2 = 'https://www.financialexpress.com/?search_scope=1&s=' + l
        response_2 = requests.get(url_2)
        if response_2.status_code != 200:
            raise ConnectionRefusedError("OOPS! Can't connect to this website!")
        else:
            result_page_2 = BeautifulSoup(response_2.content, 'lxml')
            article_tags_2 = result_page_2.find_all('h3')
            text = ''
            for tag in article_tags_2:
                #    title = tag.text.strip()
                link1 = tag.a['href']
                response_tag = requests.get(link1)
                if response_tag.status_code != 200:
                    raise ConnectionRefusedError("OOPS! Can't connect to this website!")
                else:
                    result_page = BeautifulSoup(response_tag.content, 'lxml')
                    date = result_page.find_all('span', itemprop='dateModified')
                    d = str(date)
                    dd = d[16:26].replace("-", '')
                    if dd == '':  # filter the pages without a date
                        pass
                    else:
                        date1 = datetime.strptime(dd, '%Y%m%d')
                        print(date1)
                        t1 = datetime.now() - date1
                        t2 = t1.days
                        if t2 > 30:
                            pass
                        else:
                            paras = result_page.find_all("p")
                            for para in paras:
                                text += para.text

        web2[l] = text
    return web2
