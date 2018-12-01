import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

#links & vars
name = 'Apple'
url = f'https://www.cnn.com/search/?size=10&q={name}&category=business'


#set chrome driver to headerless
#option_ = Options()
#option_.add_argument('--headless')

#create driver to scrape
#driver = webdriver.Chrome(chrome_options=option_)
driver = webdriver.Chrome()
driver.implicitly_wait(0.01)
driver.get(url)

# Wait 300 seconds for page to load the need elements
timeout = 300
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//h3[@class='cnn-search__result-headline']")))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()


# find_elements_by_xpath/or _by_tag_name returns an array of selenium objects.
h3_elements = driver.find_elements_by_tag_name("h3")
#find a tag with h3 tag
print(h3_elements)

#get links from a_tag uneder h3 tags
list_links = []
for h3_element in h3_elements:
    try:
        list_links.append(h3_element.find_element_by_tag_name("a").get_attribute('href'))
    except:
        continue

#get article title
#link_title_lists = [x.text for x in h3_elements]

#write out links to txt files
#with open('titles.txt', 'w') as fp:
#    for i,link in enumerate(list_links):
#        fp.write(link_title_lists[i])
#        fp.write(':\n')
#        fp.write(str(link))
#        fp.write('\n')

#close web_driver
driver.quit()

#use request here for performence ot practice selenium
#pratice selenium + multiprocess

def get_articles(list_links):

    #failure list
    list_fail_link = []
    #article text
    text = ''

    #get articles from the list_links
    for i_link in list_links:
        #set chrome driver to headerless
        option_ = Options()
        option_.add_argument('--headless')
        
        #create driver to scrape
        driver = webdriver.Chrome(chrome_options=option_)
        driver.get(i_link)
        
        # Wait x seconds for page to load the need elements
        timeout = 8
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='zn-body__paragraph']")))
        except TimeoutException:
            print('Timed out waiting for page to load')
            list_fail_link.append(i_link)
            driver.quit()
    
        p_elements = driver.find_elements_by_class_name("zn-body__paragraph")
        #get article and coleect all into var:text
        for p_element in p_elements:
            text = text + str(p_element.text)
        
        #clease driver
        driver.quit()
    return text
    

with open('result.txt', 'w') as fp:
    fp.write(get_articles(list_links))
#selenium click button 的方法
# [Fort Hays State University] link的按钮的 javascript element search
#python_button = driver.find_element_by_id('/.a/bundles/cnn-header.421e289332a74a2f369f-first-bundle.js') #FHSU
#python_button.click()


#用来看网站的 原代码 看看
#response = requests.get(url)
#print(response)
#Soup = BeautifulSoup(response.content, 'lxml')
#print(Soup.prettify())
#with open('Soup.txt', 'w') as fp:
#    fp.write(str(Soup.prettify()))

