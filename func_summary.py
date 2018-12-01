"""
summary function: get the a short version of the test
input:
    data_root: file root
    file_name: the file need to summary
    line: lines of the summary
output:
    text of summary
"""
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import collections
from nltk.corpus import PlaintextCorpusReader
def get_summary(data_root,file_name,lines = 5):
    # key: the original sentences. value: the lowercase version of the sentences
    new_sentences = {}
    # key: the original sentences. value: the sum of the frequencies of each word in the sentence
    new_sentence_counts = {}
    # get raw data from a file
    text_data = PlaintextCorpusReader(data_root, file_name)
    text = text_data.raw()
    summary = ''
    # get a word list without stopword
    strip_text = text.replace('\n\n', ' ')
    strip_text = strip_text.replace('\n', ' ')
    words = word_tokenize(strip_text)

    # get word frequencies
    lowercase_words = [word.lower() for word in words
                       if word not in stopwords.words() and word.isalpha()]
    article_length = len(lowercase_words)

    # decide the number of words with high frequencies
    word_frequencies = FreqDist(lowercase_words)
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
        summary += items
    return summary
dataroot = ''
filename = 'apple_filtered.txt'
print(get_summary(dataroot,filename,5))
