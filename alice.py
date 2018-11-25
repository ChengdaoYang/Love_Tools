import requests
import re
from bs4 import BeautifulSoup
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
print(data)
