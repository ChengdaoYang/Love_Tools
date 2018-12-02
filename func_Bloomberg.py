import time
# get the text from bloomberg and return news 
def get_Bloomberg(name, day, out_put = False, debug = False):
    
    url = "https://www.bloombergquint.com/search?q=" + name
    try:
    #request the url, Soup parse and get tag of each relavent article
        response = requests.get(url)  
        containers = BeautifulSoup(response.content,'lxml')
        if response.status_code != 200:
            return ""
    
        text = ""
        for container in containers.find_all("li",{"class":"topic-page__item"}):
    
            link = "https://www.bloombergquint.com" + container.h3.a["href"]
            t = container.time["datetime"]
            delta = round((time.time() - float(t[:-3]))/86400,2)
            if delta > day:
                if debug:
                    print('delta break')
                break
            
            try: 
                response = requests.get(link)
                if response.status_code != 200:
                    if debug:
                        print('error get paragraph')
                    break
                page = BeautifulSoup(response.content,'lxml')
                paragraphs = page.find_all("p")
        
                for paragraph in paragraphs:
                    text = text + ' ' + paragraph.text
            except:
                continue               
        if out_put:
            with open(f'{name}_bloomberg.txt', 'w', encoding="utf-8") as fp:
                fp.write(text)
                
        return text
    except:  
        return ""
'''    
a = get_Bloomberg('Apple', day = 30, out_put = False)
print(a)
'''
