'''
 function use: filter the txt file and return the sentences containing a specific company name
 input:
    text: need to be filtered and
    search_word: use to be filtered
  text has been filtered
'''
import re
search_word = 'Apple'
def get_filtered(text, search_word, out_put = False):
    strip_text = text.replace('\n\n', ' ')
    strip_text = strip_text.replace('\n', ' ')
    sentences = re.split('\. |\; |\? |\! ', strip_text)
    print(sentences)
    filtered_text = ""
    for i in range(len(sentences)):
        line1 = sentences[i]
        if line1 != None and line1 not in filtered_text:
            if search_word in line1:
                line_with_dot = line1 + '. '
                filtered_text += line_with_dot
    if out_put:
        with open(f'{search_word}_filtered.txt', 'w') as fp:
            fp.write(filtered_text)
    return filtered_text