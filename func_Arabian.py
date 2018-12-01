import requests
from bs4 import BeautifulSoup
import datetime

string1 = 'apple'
#21
def get_Arabian(name, date_, out_put = False):
    web21 = {}
    #for l in lists:
    url_21 = 'https://www.arabianbusiness.com/search?q=' + name + '&sort=date'
    response_21 = requests.get(url_21)
    if response_21.status_code != 200:
        raise ConnectionRefusedError("OOPS! Can't connect to this website!")
    else:
        result_page_21 = BeautifulSoup(response_21.content, 'lxml')
        article_tags_21 = result_page_21.find_all('h3', class_='g-tit')
        text = ''
        for tag in article_tags_21:
        #    title = tag.text.strip()
            link1 = tag.a['href']
            link = 'https://www.arabianbusiness.com' + link1
            response_tag = requests.get(link)
            if response_tag.status_code != 200:
                raise ConnectionRefusedError("OOPS! Can't connect to this website!")
            else:
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
                    if t2 > date_:
                        pass
                    else:
                        paras = result_page.find_all("p")
                        for para in paras:
                            text += para.text
        if out_put:
            with open(f'{name}_AB_news.txt', 'w') as fp:
                fp.write(text)
        return text
'''
try
    print(website21(lists))
except requests.ConnectionError as e:
    print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
    print(str(e))
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
    print(str(e))
except requests.RequestException as e:
    print("OOPS!! General Error")
    print(str(e))
except KeyboardInterrupt:
    print("Someone closed the program")

'''
