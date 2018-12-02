
from func_weekly import get_weekly         
from func_signal import get_signal 
from func_eight_emotion import get_eight_emotion
from func_daily_news import get_daily_news
from func_pos_neg import get_pos_neg_words
from func_pos_neg import get_pos_neg_stock
from func_filter import get_filtered


def get_backtest(ticker, day):
    dic = get_daily_news(ticker, day, out_put = False)
    positive_words,negative_words = get_pos_neg_words()

    for date_ in dic.keys():
        text = dic[date_]
        text = get_filtered(ticker, text, out_put = False)
        # predict
        eight_emotion = get_eight_emotion(text)    
        pos_neg = get_pos_neg_stock(text)
        predict = get_signal(pos_neg,eight_emotion, threshold = 1.5)
        # reality
        real = get_weekly(ticker, date_)
        return (str(date_),predict,real)

