
from nltk import word_tokenize
# Return positive and negative words 

     
# Input text 
# Output ---> position /negative 
def get_signal(text, threshold = 1.5):
    
    def get_pos_neg_words():
        def get_words(url):
            import requests
            words = requests.get(url).content.decode('latin-1')
            word_list = words.split('\n')
            index = 0
            while index < len(word_list):
                word = word_list[index]
                if ';' in word or not word:
                    word_list.pop(index)
                else:
                    index+=1
            return word_list
    
        #Get lists of positive and negative words
        p_url = 'http://ptrckprry.com/course/ssd/data/positive-words.txt'
        n_url = 'http://ptrckprry.com/course/ssd/data/negative-words.txt'
        positive_words = get_words(p_url)
        negative_words = get_words(n_url)
        return positive_words,negative_words
    
    try:
        positive_words
    except:
        positive_words,negative_words = get_pos_neg_words()

# input text --> 
# output positive and negtive percentage
    def get_pos_neg_stock(text):
        pos = neg = 0
        from nltk import word_tokenize
        number = len(word_tokenize(text))
        for word in word_tokenize(text):
            if word in positive_words:
                pos+=1
            if word in negative_words:
                neg+=1
        if number == 0:
            return 0,0
        return pos/number*100,neg/number*100
    
#Input stock news --> string
#Output 8 emotions
#NRC data codifies words with emotions
#14,182 words are coded into 2 sentiments and 8 emotions    

    def get_NRC_data():
        # Read text and return emotion words
        count=0
        emotion_dict=dict()
        with open("emotion_words.txt","r") as f:
            for line in f:
                if count < 46:
                    count+=1
                    continue
                line = line.strip().split('\t')
                if int(line[2]) == 1:
                    if emotion_dict.get(line[0]):
                        emotion_dict[line[0]].append(line[1])
                    else:
                        emotion_dict[line[0]] = [line[1]]
        return emotion_dict

    def get_emotion_analyzer(text,emotion_dict):
        #Set up the result dictionary
        emotions = {x for y in emotion_dict.values() for x in y}
        emotion_count = dict()
        for emotion in emotions:
            emotion_count[emotion] = 0
    
        #Analyze the text and normalize by total number of words
        for word in text.split():
            if emotion_dict.get(word):
                for emotion in emotion_dict.get(word):
                    emotion_count[emotion] += 1/len(text.split())
        return emotion_count
        
    emotion_dict = get_NRC_data()        
    eight_emotion = get_emotion_analyzer(text,emotion_dict)  
    pos_neg = get_pos_neg_stock(text)      
    
    eight_emotion['Pos'] = eight_emotion['trust'] + eight_emotion['positive'] + eight_emotion['joy'] + eight_emotion['anticipation']
    eight_emotion['Neg'] = eight_emotion['fear'] + eight_emotion['negative'] + eight_emotion['disgust'] + eight_emotion['sadness']

    if eight_emotion["Neg"] != 0:
         if eight_emotion["Pos"]/eight_emotion["Neg"] >  threshold:
            return 1
    elif eight_emotion["Pos"] != 0:
        if eight_emotion["Neg"]/eight_emotion["Pos"] >  threshold:
            return -1
    elif pos_neg[0] != 0:
        if pos_neg[1]/pos_neg[0] >  threshold:
            return 1
    elif pos_neg[1] != 0:
        if pos_neg[0]/pos_neg[1] >  threshold:
            return -1
    else:
        return 0
        

#a = get_signal(text, threshold = 1.5)
#print(a)

    
