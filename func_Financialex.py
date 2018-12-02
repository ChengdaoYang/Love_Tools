# website: http://www.financialexpress.com/
# input: company name, timedelta, out_put(determine whether to write the text to a file)

import requests
from bs4 import BeautifulSoup
import datetime


def get_Financialex(name, date_, out_put = False):
    url_2 = 'https://www.financialexpress.com/?search_scope=1&s=' + name
    try:
        response_2 = requests.get(url_2)
        if response_2.status_code != 200:
            return ''
        else:
            result_page_2 = BeautifulSoup(response_2.content, 'lxml')
            article_tags_2 = result_page_2.find_all('h3')
            text = ''
            for tag in article_tags_2:
                #    title = tag.text.strip()
                link1 = tag.a['href']
                try:
                    response_tag = requests.get(link1)
                    if response_tag.status_code != 200:
                        return ''
                    else:
                        result_page = BeautifulSoup(response_tag.content, 'lxml')
                        date = result_page.find_all('span', itemprop='dateModified')
                        d = str(date)
                        dd = d[16:26].replace("-", '')
                        if dd == '':  # filter the pages without a date
                            pass
                        else:
                            date1 = datetime.datetime.strptime(dd, '%Y%m%d')
                            #print(date1)
                            t1 = datetime.datetime.now() - date1
                            t2 = t1.days
                            if t2 > date_:
                                pass
                            else:
                                paras = result_page.find_all("p")
                                for para in paras:
                                    text += para.text
                except:
                    continue
            if out_put:
                with open(f'{name}_FE_news.txt', 'w') as fp:
                    fp.write(text)
            return text
    except:
        return ''