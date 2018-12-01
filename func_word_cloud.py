# install wordcloud
# enter "pip3 install wordcloud" in terminal

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
def get_word_cloud_picture(filename):
    f = open(filename,'r')
    text = f.read()
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=3000,height=3000).generate(text)
    return wordcloud
'''
plt.imshow(get_word_cloud_picture('apple_filtered.txt'))
plt.axis('off')
plt.show()
'''
