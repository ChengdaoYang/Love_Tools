
def get_Eight_emotion(text):
#Input stock news --> string
#Output 8 emotions
#NRC data codifies words with emotions
#14,182 words are coded into 2 sentiments and 8 emotions    
    def get_Emotion_data():
        # Get NRC sentiment data and save to text 
        # Return a text name
        url = '''https://raw.githubusercontent.com/sebastianruder/emotion_proposition_store/
         master/NRC-Emotion-Lexicon-v0.92/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'''
        words = requests.get(url).content.decode('latin-1')
        nrc = 'emotion_words.txt'        
        with open(nrc,'w') as fp:
            fp.write(words) 
        pass  

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

    def get_Emotion_analyzer(text,emotion_dict):
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
    
        
    try:
        open('emotion_words.txt','r')
    except FileNotFoundError:
        get_Emotion_data() 
        
    emotion_dict = get_NRC_data()        
    result = get_Emotion_analyzer(text,emotion_dict)
    
    return ("%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f\t%1.2f"%(
        result['fear'],result['trust'],
          result['negative'],result['positive'],result['joy'],result['disgust'],
          result['anticipation'],result['sadness'],result['surprise']))

#get_Eight_emotion(text)