import requests
from bs4 import BeautifulSoup
import time

lists = ['apple', 'starbucks']
#21
def website21(my_list):
    web21 = {}
    for l in lists:
        url_21 = 'https://www.arabianbusiness.com/search?q=' + l + '&sort=date'
        response_21 = requests.get(url_21)
        result_page_21 = BeautifulSoup(response_21.content, 'lxml')
        article_tags_21 = result_page_21.find_all('h3', class_='g-tit')
        text = ''
        for tag in article_tags_21:
        #    title = tag.text.strip()
            link1 = tag.a['href']
            link = 'https://www.arabianbusiness.com' + link1
            respons = requests.get(link)
            result_page = BeautifulSoup(respons.content, 'lxml')
            date = result_page.find_all('div',class_= 'date')
            d = str(date)
            dd = d[23:35]
            print(dd)
            if not dd[3:6] == 'Nov':
                break
            paras = result_page.find_all("p")
            for para in paras:
                text += para.text
        web21[l] = text
    return web21
print(website21(lists))
