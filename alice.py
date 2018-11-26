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
def website19():
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




# analyzes emotions
def get_pos_neg_words():
    def get_words(url):
        import requests
        words = requests.get(url).content.decode('latin-1')
        word_list = words.split('\n')
        index = 0
        while index < len(word_list):
            word = word_list[index]
            if ';' in word or not word:
                word_list.pop(index)
            else:
                index+=1
        return word_list

    #Get lists of positive and negative words
    p_url = 'http://ptrckprry.com/course/ssd/data/positive-words.txt'
    n_url = 'http://ptrckprry.com/course/ssd/data/negative-words.txt'
    positive_words = get_words(p_url)
    negative_words = get_words(n_url)
    return positive_words,negative_words

positive_words,negative_words = get_pos_neg_words()

def analyze_emotions(result):
    data =[]
    for i in range(len(result)):
        text = result[i]
    #     print(text[0])

        number = len(word_tokenize(text[2]))
        pos = neg = 0
        for word in word_tokenize(text[2]):
            if word in positive_words:
                pos+=1
            if word in negative_words:
                neg+=1

        data.append([text[0],pos/number*100,neg/number*100])

    data = pd.DataFrame(data,columns = ['title','positive%','negative%']) 

    return data

import pandas as pd
















    




