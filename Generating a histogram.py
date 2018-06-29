import os
import np
os.chdir('C:\\Users\\yeachan153\\Desktop\\Text-Collection')
from TextCollect import *

hash_table = TextCollect('txt-for-assignment-data-science.txt')
hash_table.read_data()
hash_table.split_list()
hash_table.remove_tags()
hash_table.punctuation()
hash_table.singular()
hash1 = hash_table.word_dict()

keys = [key for key in hash1]

counter_list = list(hash1.values())
num_list = len(counter_list[0])

for idx, current_list in enumerate(counter_list):
    counter_list[idx] = sum((current_list[0:num_list]), Counter())

total = np.array([counter_list[i][keys[i]] for i in range(len(counter_list))])

