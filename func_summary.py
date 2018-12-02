#decription of the funcion:
"""
summary function: get the a short version of the text and get wordcloud picture of the text(optional)
input:
    name: name of the company
    text: the text need to be filtered
    line: lines of the summary
    plot: decide whether to plot word_cloud picture
    out_put: whether to save a summary.txt file
output:
    text of summary
first install wordcloud
enter "pip3 install wordcloud" in terminal
"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import collections
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from func_filter import get_filtered

#summary return a summay of all news on scraped of a company, with option of plot and/or save the word cloud image
def get_summary(company, day=7, lines = 4, plot = False, save_plot=False, out_put = False):
    text = company.news(day=day)
    # key: the original sentences. value: the lowercase version of the sentences
    new_sentences = {}
    # key: the original sentences. value: the sum of the frequencies of each word in the sentence
    new_sentence_counts = {}


    #calling the filtere function in the same dir to filter the news with only self.keyword
    text = get_filtered(search_word=company.keyword, text=text)
    

    with open('text_input_to_summary.txt', 'w') as fp:
            fp.write(text)
    text_data = PlaintextCorpusReader('','text_input_to_summary.txt')
    text = text_data.raw()
    strip_text = text.replace('\n\n', ' ')
    strip_text = strip_text.replace('\n', ' ')
    strip_text = strip_text.replace('.', '. ')
    words = word_tokenize(strip_text)
    summary = ''
    # get word frequencies
    lowercase_words = [word.lower() for word in words
                       if word not in stopwords.words()]
    article_length = len(lowercase_words)

    # decide the number of words with high frequencies
    # word_frequencies = FreqDist(lowercase_words)
    freq_word_number = round(article_length * 0.04)
    most_freq_words = FreqDist(lowercase_words).most_common(freq_word_number)

    # count most_freq_words in every line
    sentences = sent_tokenize(strip_text)
    for sentence in sentences:
        new_sentences[sentence] = sentence.lower()
    for upper, lower in new_sentences.items():
        count = 0
        for freq_word, frequency_score in most_freq_words:
            if freq_word in lower:
                count += frequency_score
                new_sentence_counts[upper] = count

    #get the summary
    sorted_sentences = collections.OrderedDict(sorted(
                        new_sentence_counts.items(),
                        key = lambda x: x[1],
                        reverse = True)[:lines])
    for items in sorted_sentences:
        summary = summary + ' ' + items
    summary = ' '.join(summary.split())
    summary.replace(' ,',',')

    # if you decided to draw a wordcloud picture
    if plot == True:
        wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=3000, height=2500,
                              max_words=50).generate(text)
        plt.figure(1, figsize=(13, 13))
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.title('Wordcloud picture')



    if save_plot:
        # Turn interactive plotting off
        plt.ioff()
        
        wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=3000, height=2500,
                              max_words=50).generate(text)

        plt.imshow(wordcloud)
        plt.axis('off')
        plt.title('Wordcloud picture')
        plt.savefig(f'{company.ticker}.png')
        plt.close()
        
    if out_put:
        with open(f'{company.keyword}_summary.txt', 'w') as fp:
            fp.write(summary)
    return summary


#c = open('Amazon_filtered.txt','r')
#r = c.read()
#print(get_summary('amzn', r,1, True, False))

