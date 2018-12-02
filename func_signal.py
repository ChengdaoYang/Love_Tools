
# Input pos_neg --> tuple, eight_emotion --> dictionary 
def get_signal(pos_neg,eight_emotion, threshold = 1.5):
    
    
    eight_emotion['Pos'] = eight_emotion['trust'] + eight_emotion['positive'] + eight_emotion['joy'] + eight_emotion['anticipation']
    eight_emotion['Neg'] = eight_emotion['fear'] + eight_emotion['negative'] + eight_emotion['disgust'] + eight_emotion['sadness']

    list_pos = [eight_emotion["Pos"]/eight_emotion["Neg"],pos_neg[1]/pos_neg[0]]
    list_neg = [eight_emotion["Neg"]/eight_emotion["Pos"],pos_neg[0]/pos_neg[1]]
             

    if any(ratio >  threshold for ratio in list_pos) :
        return 1
    elif any(ratio >  threshold for ratio in list_neg) :
        return -1
    else:
        return 0



    
