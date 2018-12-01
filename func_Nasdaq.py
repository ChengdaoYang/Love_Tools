
def get_Nasdaq(name，date_, out_put = False):
    text = "" 
    count = 1
    flag = True
    while (count <= 20 and flag):
        url = 'https://www.nasdaq.com/symbol/'+name+'/news-headlines?page=' + str(count)        
        response = requests.get(url)
        containers = BeautifulSoup(response.content,'lxml')      
        containers_news = containers.find("div",{"class":"news-headlines"})
        for container in containers_news.find_all("div"):
            if container.small is not None:
                t = str(container.small)
                pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
                match = re.findall(pattern,t)
                if match == []:
                    continue
                public_date = datetime.datetime.strptime(match[0], '%m/%d/%Y')
                today = datetime.datetime.today()
                delta = (today - public_date).days
                if delta > date_:
                    flag = False
                    break       
                link = container.a['href']
                response = requests.get(link)
                page = BeautifulSoup(response.content,'lxml')                     
                paragraphs = page.find_all("p")                   
                for paragraph in paragraphs:          
                    text += paragraph.text            
        count += 1   
        
    if out_put:
        with open(f'{name}_nasdaq.txt', 'w', encoding="utf-8") as fp:
            fp.write(text) 
      
    return text   

# web_nasdaq('amzn',7,True)
                  
                
   