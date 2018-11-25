import requests
import re
from bs4 import BeautifulSoup
# website 15
def website15():
    url = 'https://www.thehindubusinessline.com/'
    response = requests.get(url)
    containers = BeautifulSoup(response.content,'lxml')
    data = []
    for container in containers.find_all("h4"):
        container_title = container.text
        container_link = container.a['href']

        response = requests.get(container_link)
        page = BeautifulSoup(response.content,'lxml')
        paragraphs = page.find_all("p")
        text = ""
        for paragraph in paragraphs:
            text += paragraph.text

        data.append((container_title,container_link,text))

    return(data)
# website 7
def website7():
    url = "https://www.morningstar.com/"
    response = requests.get(url)
    containers = BeautifulSoup(response.content,'lxml')
    response.status_code
    data = []
    for abc in containers.find_all("div",{"class":"article-lineup-item section"}):

        if abc.a['href'][0] == '/':
            container_link = 'https://www.morningstar.com/' + abc.a['href']
            match = re.search(r'\d/(.+?).html',container_link)
            container_title = match.groups()[0]

            response = requests.get(container_link)
            page = BeautifulSoup(response.content,'lxml')
            paragraphs = page.find_all("p")
            text = ""
            for paragraph in paragraphs:
                text += paragraph.text

            data.append((container_title,container_link,text))

    return(data)
# website 19
def website19()
    data = []
    for container in containers.find_all("article",{"class":"topnews__story"}):
        container_title = container.text
        container_title = ' '.join(container_title.split())
        container_link = 'https://www.bloombergquint.com/' + container.a['href']

        response = requests.get(container_link)
        page = BeautifulSoup(response.content,'lxml')
        paragraphs = page.find_all("p")
        text = ""
        for paragraph in paragraphs:
            text += paragraph.text

        data.append((container_title,container_link,text))
        
    return(data)



















    




