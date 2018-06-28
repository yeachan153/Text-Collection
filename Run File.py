import os
from collections import Counter
import numpy as np
import inflect
import re

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
        split_list.append(list_words[split_indexes[idx - 1] + 2:split_indexes[idx]])

    # Remove tags
num_doc = len(split_list)

remove = list(
    set(['<docno>', '<docid>', '<date>', '<p>', '</p>', '</date>', '<section>', '</section>', '<length>', '</length>',
         '<headline>', '</headline>', '<byline>', '</byline>', '<text>', '</text>', '<graphic>', '</graphic>', '<type>',
         '</type>', '</docno>', '</docid>']))

for i in range(num_doc):
    for each_tag in remove:
        split_list[i] = list(filter(lambda x: x != each_tag, split_list[i]))

# Remove punctuation and empty lists
split_list2 = []
for i in range(num_doc):
    current_list = split_list[i]
    for idx, each_word in enumerate(current_list):
        current_list[idx] = re.sub('[^a-zA-Z0-9]+', '', each_word)
    current_list = list(filter(None, current_list))
    split_list2.append(current_list)

# Converting plurals to singular...
num_doc = len(split_list2)       
split_list3 = [] 

p = inflect.engine()
for each_list in split_list2:
    current_list = each_list        
    for idx, each_word in enumerate(current_list):
        singular = p.singular_noun(each_word) 
        if singular == False:
            current_list[idx] = each_word
        elif singular != False:
            current_list[idx] = singular
    split_list3.append(current_list)

# Into a hash   
hash_table = {}

num_doc = len(split_list3)

for idx, current_list in enumerate(split_list3):    
    for current_word in current_list:
        if current_word not in hash_table:
            hash_table[current_word] = [Counter() for i in range(num_doc)]
            hash_table[current_word][idx].update([current_word])
        elif current_word in hash_table:
            hash_table[current_word][idx].update([current_word])


