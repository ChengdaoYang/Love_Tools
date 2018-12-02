"""
summary function: get the a short version of the test
input:
    text: the text need to be filtered
    name: name of the company
    line: lines of the summary
output:
    text of summary
"""
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import collections
def get_summary(text, name, lines = 5, out_put = False):
    # key: the original sentences. value: the lowercase version of the sentences
    new_sentences = {}
    # key: the original sentences. value: the sum of the frequencies of each word in the sentence
    new_sentence_counts = {}
    # get a word list without stopword
    with open('text_input_to_summary.txt', 'w') as fp:
            fp.write(text)
    text_data = PlaintextCorpusReader('','text_input_to_summary.txt')
    text = text_data.raw()
    strip_text = text.replace('\n\n', ' ')
    strip_text = strip_text.replace('\n', ' ')
    words = word_tokenize(strip_text)
    summary = ''
    # get word frequencies
    lowercase_words = [word.lower() for word in words
                       if word not in stopwords.words() and word.isalpha()]
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
        summary += items
    if out_put:
        with open(f'{name}_summary.txt', 'w') as fp:
            fp.write(summary)
    return summary
