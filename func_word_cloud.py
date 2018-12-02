# first install wordcloud
# enter "pip3 install wordcloud" in terminal

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
def get_word_cloud_picture(filename):
    f = open(filename,'r')
    text = f.read()
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=3000,height=2500,max_words=50).generate(text)
    plt.figure(1,figsize=(13, 13))
    plt.axis('off')
    plt.title('Wordcloud picture')
    plt.savefig('wordcloud.png')
    print(type('wordcloud'))
    return wordcloud

plt.imshow(get_word_cloud_picture('Amazon_filtered.txt'))

