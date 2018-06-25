import os
from collections import Counter
import numpy as np
import inflect

os.chdir('C:\\Users\\yeachan153\\Desktop\\Text-Collection')

# Reading in file, converting all to lowercase
with open('txt-for-assignment-data-science.txt', 'r') as text:
    string_obj = text.read()
    list_words = string_obj.lower().split()

    
# Splitting into lists for each doc
split_indexes = [idx for idx, word in enumerate(list_words) if word == '</doc>']

split_list = []
for idx, i in enumerate(split_indexes):
    if idx == 0:
        split_list.append(list_words[1:split_indexes[idx]])
    else:
        split_list.append(list_words[split_indexes[idx-1]+2:split_indexes[idx]]) 

# Remove tags
num_doc = len(split_list)  

remove = list(set(['<docno>', '<docid>', '<date>', '<p>', '</p>', '</date>','<section>','</section>','<length>','</length>',
          '<headline>','</headline>','<byline>','</byline>','<text>','</text>','<graphic>','</graphic>','<type>',
          '</type>','</docno>','</docid>']))

for i in range(num_doc):
    for each_tag in remove:
        split_list[i] = list(filter(lambda x: x != each_tag, split_list[i]))

# Remove punctuation


# Converting plurals to singular...
num_doc = len(split_list)        

p = inflect.engine()
test = split_list[0][165:180]
for idx, each_word in enumerate(test):
    singular = p.singular_noun(each_word) 
    if singular != False:
        test[idx] = singular


       


def collect_frequencies(nameoffile):
    with open(nameoffile, "r", encoding = 'utf8') as text:
        string_obj = text.read()
        individual_words = string_obj.lower().split()
        return dict(Counter(individual_words))

dict1 = collect_frequencies('txt-for-assignment-data-science.txt')
