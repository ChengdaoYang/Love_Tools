mport requests
import re
from bs4 import BeautifulSoup
url = 'https://www.thehindubusinessline.com/'
response = requests.get(url)
results_page = BeautifulSoup(response.content,'lxml')
#print(results_page.prettify())
#for link in results_page.find_all("a"):
#      print(link.get('href'))
for link in soup.findAll('a',attrs = {'href':re.compile("^http")}):
    print(link)
