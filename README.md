Welcome to Love_Tools’s Team project :blush:
===================================
![Our Team](https://raw.githubusercontent.com/ChengdaoYang/Love_Tools/master/Team_Pic.png "Our Team")
===================================
## Repository
* [What is it?](#What-is-it?)
* [Main Feature](#Main-Feature)
* [How to operate it?](#How-to-operate-it?)
* [Required Modules](#Required-Modules)
* [Drawbacks](#Drawbacks)
* [Further Developments](#Further-Developments)
* [Group Members](#Group-Members)

### What is it?
Love_Tools is an automatic mail sent tools that track the stock maket. It sent specific stock news summary every week and sent prediction based on weekly news.
***********
### Main Feature
* Scrape main financial websit such as Yahoo, Nasdaq, CNN, Financial Express and extract stock market data using Python and LXML
* Get content from dynamic web page with Selenium WebDriver
* Clean news data and get stock related setences
* Get the summary from history news
* Generate word cloud and create tag cloud
* Sent email regularly
* Use text mining and sentiment analysis to understand the positive or negative opinion expressed by news
*************
### How to operate it?
*****************
### Required Modules
##### Web Scraping
&emsp requests, bs4.BeautifulSoup
##### Text Mining
&emsp nltk.word_tokenize
##### Summary & Words Cloud
&emsp nltk.tokenize, nltk.corpus, wordcloud, collections
##### Sent Email
&emsp email, smtplib
##### Other basic library
&emsp datetime, time, re, random, matplotlib.pyplot
*****************
### Drawbacks
Time complexity may be a little high. It take a little long time to repeat reading news.
************
### Further Developments
Build a graphical user interface to make it more user-friendly
********************
### Group Members
- Yangdao Cheng
- Wansi Xie
- Manchun Sun
- Xiangdong Duan
****************
