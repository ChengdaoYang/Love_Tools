import requests
from bs4 import BeautifulSoup

'''
url = 'https://www.cnbc.com/world/?region=world '
response = requests.get(url)
result_page = BeautifulSoup(response.content,'lxml')
div_a_tags = result_page.find_all('a')
#print(result_page)
ww =[]
for tag in div_a_tags:
    ww.append(tag.get('href'))
print(ww)
'''

'''
#13
url = 'https://www.financialexpress.com/?search_scope=1&s=stock'
response = requests.get(url)
result_page = BeautifulSoup(response.content,'lxml')
article_tags = result_page.find_all("h3")
#article_tags = result_page.find_all('div', {'class':'textDiv'})
web13 = []
for tag in article_tags:
    title = tag.text.strip()
    link = tag.a['href']
    respons = requests.get(link)
    result_page = BeautifulSoup(respons.content, 'lxml')
    paras = result_page.find_all("p")
    text = ''
    for para in paras:
        text += para.text
    web13.append((title, link, text))

print(web13)
'''

'''
#17
url_17 = 'https://www.financialexpress.com/?search_scope=1&s=stock'
response_17 = requests.get(url_17)
result_page_17 = BeautifulSoup(response_17.content, 'lxml')
article_tags_17 = result_page_17.find_all('h3')
web17 = []
for tag in article_tags_17:
    title = tag.text.strip()
    link = tag.a['href']
    respons = requests.get(link)
    result_page = BeautifulSoup(respons.content, 'lxml')
    paras = result_page.find_all("p")
    text = ''
    for para in paras:
        text += para.text
    web17.append((title, link, text))
'''

'''
#21
url_21 = 'https://www.arabianbusiness.com/search?q=stock&sort=date'
response_21 = requests.get(url_21)
result_page_21 = BeautifulSoup(response_21.content, 'lxml')
article_tags_21 = result_page_21.find_all('h3',class_='g-tit')
web21 = []
for tag in article_tags_21:
    title = tag.text.strip()
    link1 = tag.a['href']
    link = 'https://www.arabianbusiness.com' + link1
    print(link)
    respons = requests.get(link)
    result_page = BeautifulSoup(respons.content, 'lxml')
    paras = result_page.find_all("p")
    text = ''
    for para in paras:
        text += para.text
    web21.append((title, link, text))

'''

#web25
url_21 = 'https://www.arabianbusiness.com/search?q=stock&sort=date'
response_21 = requests.get(url_21)
result_page_21 = BeautifulSoup(response_21.content, 'lxml')
article_tags_21 = result_page_21.find_all('h3',class_='g-tit')
web21 = []
for tag in article_tags_21:
    title = tag.text.strip()
    link1 = tag.a['href']
    link = 'https://www.arabianbusiness.com' + link1
    print(link)
    respons = requests.get(link)
    result_page = BeautifulSoup(respons.content, 'lxml')
    paras = result_page.find_all("p")
    text = ''
    for para in paras:
        text += para.text
    web21.append((title, link, text))
print(web21[0])