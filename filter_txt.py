'''
n use: filter the txt file and return the sentences containing a specific company name
 input:
  file_name: this is the name of the file you want to filter
  my_list: a list of the company name and the stock abbreviation you want to filter

 output: the text has been filtered
'''
import re
list1 = ['Apple','AAPL']
def filter(file_name, my_list):
    f = open(file_name,'r')
    c = f.read()
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', c)
    text1 = ""
    pattern = r''
    for i in range(len(sentences)):
        line1 = sentences[i]
        if sentences[i] != None:
            if my_list[0] in line1 or my_list[1] in line1:
                line2 = line1 + '.'
                text1 += line2
    return text1
    #pattern = r'^'
print(get_string('result.txt',list1))
