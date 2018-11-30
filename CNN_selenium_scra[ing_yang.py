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

url = 'https://www.cnn.com/search/?size=10&q=Apple&category=business'


driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get(url)

# Wait 20 seconds for page to load
timeout = 300
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//h3[@class='cnn-search__result-headline']")))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()


# find_elements_by_xpath returns an array of selenium objects.
titles_element = driver.find_elements_by_tag_name("h3")

#find a tag with h3 tag
list_links = []
for h3_element in titles_element:
    list_links.append(h3_element.find_element_by_tag_name("a").get_attribute('href'))
# use list comprehension to get the actual repo titles and not the selenium objects.
#titles = [x.text for x in titles_element]

# print out all the titles.
print('titles:')
#print(titles, '\n')

#with open('titles.txt', 'w') as fp:
#    for link in list_links:
#        fp.write(str(link))
#        fp.write('\n')
# [Fort Hays State University] link的按钮的 javascript element search
#python_button = driver.find_element_by_id('/.a/bundles/cnn-header.421e289332a74a2f369f-first-bundle.js') #FHSU
#python_button.click()


#response = requests.get(url)
#print(response)
#Soup = BeautifulSoup(response.content, 'lxml')
#print(Soup.prettify())
#with open('Soup.txt', 'w') as fp:
#    fp.write(str(Soup.prettify()))

