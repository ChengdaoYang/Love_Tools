Welcome to Love_Tools’s Team project :blush:
===================================
![Our Team](https://raw.githubusercontent.com/ChengdaoYang/Love_Tools/master/image/Team_Pic.png "Our Team")
===================================
## Lovely_Tools Repository
* [What is it](#What-is-it)
* [Main Feature](#Main-Feature)
* [Installation](#Installation)
* [How to operate it](#How-to-operate-it)
* [Sample](#Sample)
* [Further Developments](#Further-Developments)
* [Group Members](#Group-Members)

### What is it
Lovely_Tools is the best friend of financial analysts. 
It reads new on Internet (_such as Bloomberg, CNN, Yahoo Finance, Nasdaq and so on_), summaries news, predicts stocks, tracks stock markets, and sends emails and notifications. 
<br/>
(A secret: we can see when users run it.)
***********
### Main Feature
* _Read News:_ get the news from 7 major financial websites
* _News Summary:_ summary history news from the 7 major websites
* _Stock Monitor:_ analysis stock news and send emails on regular time (can be 1 hour, 10 minutes, 2 days and so on)
* _Stock Prediction:_ predict stock trend 
* _Send Email:_ send an email with stock analysis data and picture
* _Backtest:_ test if the history news shows the same trend as the real stock data
*****************
### Installation
##### Requirements
Lovely_Tools relys on requests, bs4, selenium, ntlk, collections, random, matplotlib, time, datetime, 
smtplib, email. Thanks them XD. <br/>
(_requirement.txt_)

*************
### How to operate it
Analysts can create Company objects with Lovely_Tools, based on company's name, if the company is listed on stock markets.
Then they can simply call its method and attributes.<br/>
Fistly, create an instance and enter your email address:
``` {.sourceCode .python}
>>> c = Company('apple')
please type your email address, to recieve notification of monitoring stocks...
```
#### Attributes
- keyword: get the name of the company
``` {.sourceCode .python}
>>> c.keyword
Apple
```
- ticker: get the ticker symbol of the stock 
(from Yahoo website)

``` {.sourceCode .python}
>>> c.ticker
AAPL
```
#### Methods
- **monitor**() <br/>
Send email to analysts at regular time. Don't forget to sleep it by calling it twice. <br/>
This a very very awesome method, try it!  :) <br/>
see _example.py_ for detail
``` {.sourceCode .python}
>>> c.monitor()
...opening monitor function...
>>> c.monitor()
...closing monitor fucntion...
```
- **price**(_day=7, plot=False_)<br/>
Show the daily price in dataframe.
<table>
<tr>
    <td rowspan="4"> Parameters</td>
    <td rowspan="2">day: </td>
    <td>int, default 7</td>

</tr>
<tr>
    <td>Periods to get stock price</td>
</tr>
<tr>
    <td rowspan="2">plot: </td>
    <td>boolean, default False</td>
</tr>
<tr>
    <td>If True, save stock price line plot to relative environment. </td>
</tr>
</table>
<table>
<tr>
    <td rowspan="4"> Return</td>
    <td>Return DataFrame. Contain Highest, lowest, open, close stock price and volumn in the period
</td>
</tr>
</table>

``` {.sourceCode .python}
>>> c.price(day=30, plot=True)
```
- **news**(_day=7, out_put=False_)<br/>
Get all news of the stocks from major financial websites during a specific period. This function takes sometime. Please wait for five minutes.
<table>
<tr>
    <td rowspan="4">Parameters</td>
    <td rowspan="2">day: </td>
    <td>int, default 7</td>

</tr>
<tr>
    <td>Periods to scrape web</td>
</tr>
<tr>
    <td rowspan="2">plot: </td>
    <td>boolean, default False</td>
</tr>
<tr>
    <td>If True, save stock news to relative environment. </td>
</tr>
</table>

``` {.sourceCode .python}
>>> mynews = c.news(day=30)
>>> print(mynews)
Given rising iPhone revenue, surging services sales, and lots of room to grow in the wearable tech space, investors would be wise to consider Apple's stock right now --especially 
because the company's recent stock price dip means Apple shares are now trading at just 12 times forward earnings. Apple's (NASDAQ: AAPL) stock price has tanked about 20% over the
past three months, which has had the unfortunate effect of erasing nearly all of the company's 2018 share price gains. Each week, I'm ranking the biggest companies that trade on U. S.
...
```
- **summary**(_day=7, lines=4, plot=False, save_plot=False, out_put=False_)<br/>
Summary the news and draw a word cloud picture.
<table>
<tr>
    <td rowspan="8">Parameters</td>
    <td rowspan="2">lines: </td>
    <td>int, default 4</td>

</tr>
<tr>
    <td>Lines in summary</td>
</tr>
<tr>
    <td rowspan="2">plot: </td>
    <td>boolean, default False</td>
</tr>
<tr>
    <td>If True, plot word cloud image. </td>
</tr>
<tr>
    <td rowspan="2">save_plot: </td>
    <td>boolean, default False</td>
</tr>
<tr>
    <td>If True, save word cloud image to relative environment. </td>
</tr>
<tr>
    <td rowspan="2">out_put: </td>
    <td>boolean, default False</td>
</tr>
<tr>
    <td>If True, save summary to relative environment. </td>
</tr>
</table>

``` {.sourceCode .python}
>>> mysummary = c.summary(day=7, lines=2)
>>> print(mysummary)
In fact, for the fourth quarter of fiscal 2018, Apple's average selling price (ASP) for iPhones jumped to $793, up from $618...
```
- **email**()<br/>
Send an email with news summary, stock price, price line chart and sentiment analysis.
<br/>_see on samples_
``` {.sourceCode .python}
>>> c.email()
Start sending email...
```
- **predict**() <br/>
Read recent news and predict the stock trend in the future.<br/>
Output: _1_ the price may go up. _0_ the price may be stable. _-1_ the price may go down.
``` {.sourceCode .python}
>>> c.predict()
```
- **backtest**(_save_plot=False_) <br/>
Save a backtest plot to relative environment, the name of which is *{Company_name}_backtest.png*.
<table>
<tr>
    <td rowspan="2">Parameters</td>
    <td rowspan="2">save_plot: </td>
    <td>boolean, default False</td>

</tr>
<tr>
    <td>If True, save histogram to relative environment.</td>
</tr>
</table>

``` {.sourceCode .python}
>>> c.backtest(save_plot=True)
...saving a picture to Apple_backtest.png...
```
*****************
### Sample
#### email sample
<img width="1000" height="300" src="https://raw.githubusercontent.com/ChengdaoYang/Love_Tools/master/image/email_head.jpg"/><br/>
<img width="200" height="120" src="https://raw.githubusercontent.com/ChengdaoYang/Love_Tools/master/image/email_2.JPG"/><br/>
<img width="350" height="250" src="https://raw.githubusercontent.com/ChengdaoYang/Love_Tools/master/image/email_3.JPG"/><br/>
#### user interface sample
<img width="550" height="450" src="https://raw.githubusercontent.com/ChengdaoYang/Love_Tools/master/image/ui.jpeg"/><br/>
********************
### Further Developments
- _More Email Contents:_ The current tool can only send an email about one stock, in the future it should be able send emails on a group of stocks at the same time.
- _Solve Time Complexity:_ Since the news data are very large, we didn't save it. Everytime users call a different method, the functions have to read all the news from all the websites again. However, if we want to solve the problem of time complexity, the memory usage of the computer will be very large, but Python has no memory management, so the conflict will be very large, unfortunately, we still have difficulty solving it.
- _Improve UI_: Our UI could be more user friendly. In the future users will have better experience when using our tool. 
- _Add More Features:_ When the index exceeds threshold, the tool will only make predictions in regular daily mail. In the future, the tool should be able to send an email as soon as it detects that the prediction index exceeds the threshold.
********************
### Group Members
_All from Section 001_
- Chengdao Yang 
- Wansi Xie
- Manchun Sun
- Xiangdong Duan
****************
