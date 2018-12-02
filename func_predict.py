

from func_weekly import get_weekly         
from func_signal import get_signal 
from func_eight_emotion import get_eight_emotion
from func_daily_news import get_daily_news
from func_pos_neg import get_pos_neg_words
from func_pos_neg import get_pos_neg_stock
from func_filter import get_filtered

def get_predict(search_word, text):
    positive_words,negative_words = get_pos_neg_words()
    # predict
    text = get_filtered(search_word, text, out_put = False)
    eight_emotion = get_eight_emotion(text)    
    pos_neg = get_pos_neg_stock(text)
    predict = get_signal(pos_neg,eight_emotion, threshold = 1.5)
    return predict