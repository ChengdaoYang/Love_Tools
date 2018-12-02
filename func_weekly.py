# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:41:01 2018

@author: xws
"""
import datetime
from pandas_datareader import data as web
def get_weekly(ticker, start):
    
#    start = datetime.datetime(2018, 11, 26, 0, 0)
    end = start + datetime.timedelta(7)
    df = web.DataReader(ticker, 'yahoo', start, end)['Adj Close']
    
    ratio = df[-1]/df[0] 
    if ratio > 1.002:
        tag = 1
    elif ratio < 1/1.002:
        tag = -1
    else:
        tag = 0
    return tag
    
ticker = 'aapl'
start = datetime.datetime(2018, 11, 26, 0, 0)
get_weekly(ticker, start)
