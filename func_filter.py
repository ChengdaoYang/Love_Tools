'''
 function use: filter the txt file and return the sentences containing a specific company name
 input:
    text: need to be filtered and
    search_word: use to be filtered
  text has been filtered
'''
import re

def get_filtered(search_word, text, out_put = False):

    # strip all the text
    strip_text = text.replace('\n\n', ' ')
    strip_text = strip_text.replace('\n', ' ')
    sentences = re.split('\. |\; |\? |\! ', strip_text)
    filtered_text = ""

    # filter all the text with search_word
    for i in range(len(sentences)):
        line1 = sentences[i]
        if line1 != None and line1 not in filtered_text:
            if search_word in line1:
                line_with_dot = line1 + '. '    # give the . back in the text
                filtered_text += line_with_dot

    # whether to output filtered file
    if out_put:
        with open(f'{search_word}_filtered.txt', 'w') as fp:
            fp.write(filtered_text)
    return filtered_text
