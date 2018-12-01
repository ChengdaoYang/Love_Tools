def get_Bloomberg(name, date_, out_put = False):
    
    url = "https://www.bloombergquint.com/search?q=" + name
    response = requests.get(url)
    containers = BeautifulSoup(response.content,'lxml')
    
    text = ""
    for container in containers.find_all("li",{"class":"topic-page__item"}):

        link = "https://www.bloombergquint.com" + container.h3.a["href"]
        t = container.time["datetime"]
        delta = round((time.time() - float(t[:-3]))/86400,2)
        if delta > date_:
            break
        
        response = requests.get(link)
        page = BeautifulSoup(response.content,'lxml')
        paragraphs = page.find_all("p")

        for paragraph in paragraphs:
            text += paragraph.text
            
    if out_put:
        with open(f'{name}_bloomberg.txt', 'w', encoding="utf-8") as fp:
            fp.write(text)
            
    return text