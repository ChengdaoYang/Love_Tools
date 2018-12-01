from pandas_datareader import data as web
import datetime

def get_stock_price(ticker, day=7): 
    
    end = datetime.datetime.today()
    diff = datetime.timedelta(days = day)
    start = end - diff
    
    df = web.DataReader(ticker, 'yahoo', start, end)
    return df



#print(get_price('aapl'))
