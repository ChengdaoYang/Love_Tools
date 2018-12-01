import requests
import datetime
import parser
import re
from bs4 import BeautifulSoup

# get _url function
def get_url(name = 'apple', page = '1'):
    base_url  = f'http://fortune.com/search?q={name}&page={page}'
    return base_url

def web2():

    def get_old_day():
        now = datetime.datetime.now()
        date_delta = datetime.timedelta(days = 30)
        old_day = now - date_delta
        return old_day

    old_day = get_old_day()

    def get_url(name='apple', page='1'):
        base_url = f'http://fortune.com/search?q={name}&page={page}'
        return base_url

    url = get_url()
    # response = requests.get(url)
    # results_page = BeautifulSoup(response.content)
    # search_word = search_pages[0].get('href')[:-1]
    # aaa=112
    def find_in_one_page(url,j):
        response = requests.get(url)
        results_page = BeautifulSoup(response.content)
        all_div_tags = results_page.find_all('div',{'class':'headline heading-content-tiny margin-8-bottom media-heading'})
        data = []
        for tag in all_div_tags:
            # print(tag)
            a_tag = tag.find('a')
            data.append(a_tag.get('href'))
        selected_links = []
        for page in data:
            date_if = page[19:29]
            try:
                d = datetime.datetime.strptime(date_if, '%Y/%m/%d')
                if d > old_day:
                    selected_links.append(page)
                else:
                    j = -100
                    break
            except:
                continue
        return selected_links,j


    j = 1
    all_links = []
    while j > 0:
        url = get_url(page = str(j))
        selected_links,j = find_in_one_page(url,j)
        all_links.extend(selected_links)
        j = j + 1

    def get_content(url):
        response = requests.get(url)
        results_page = BeautifulSoup(response.content)
        all_p_tags = results_page.find_all('p')
        all_text = []
        sentences_result = []
        for i in range(len(all_p_tags)):
            all_text.append(all_p_tags[i].text)
        for text in all_text:
            if 'Apple' in text:
                sentences_result.append(text)
        return sentences_result

    all_text = []
    for i in range(len(all_links)):
        sen = get_content(all_links[i])
        all_text.extend(sen)
    return all_text
