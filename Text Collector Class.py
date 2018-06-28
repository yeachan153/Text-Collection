import os
from collections import Counter
import numpy as np
import inflect
import re
import copy
# 'txt-for-assignment-data-science.txt'

class TextCollect(object):
    def __init__(self, filepath):
        self.path = copy.deepcopy(filepath)
        self.list_of_lists = []
        self.lol_no_punc = []
        self.lol_no_plural = []
        self.hash_table = {}

    def read_data(self, lower = True):
        '''
        :param lower: True to convert all words to lowercase, otherwise False. True by default
        :return: A list of all words in file. If run first, tags, punctuation, plural words and empty spaces remain.
        '''
        with open(self.path, 'r') as text:
            string_obj = text.read()
            if lower:
                # At this point, self.data is a list
                self.list = string_obj.lower().split()
            else:
                # At this point, self.data is a list
                self.list = string_obj.split()
        return self.list

    def split_list(self):
        '''
        Splits the list into n lists where n = number of documents
        :return: Returns a list of lists. Each list represents words in each document
        '''
        split_indexes = [idx for idx, word in enumerate(self.list) if word == '</doc>']
        for idx, i in enumerate(split_indexes):
            if idx == 0:
                self.list_of_lists.append(self.list[1:split_indexes[idx]])
            else:
                self.list_of_lists.append(self.list[split_indexes[idx - 1] + 2:split_indexes[idx]])
        return self.list_of_lists

    def remove_tags(self):
        '''
        Removes the tags, e.g. '<docno>'
        :return: Returns a list of lists after removing tags.
        '''
        num_doc = len(self.list_of_lists)

        remove = list(set(['<docno>', '<docid>', '<date>', '<p>', '</p>', '</date>', '<section>', '</section>',
                           '<length>','</length>','<headline>', '</headline>', '<byline>', '</byline>', '<text>',
                           '</text>', '<graphic>', '</graphic>','<type>','</type>', '</docno>', '</docid>']))

        for i in range(num_doc):
            for each_tag in remove:
                self.list_of_lists[i] = list(filter(lambda x: x != each_tag, self.list_of_lists[i]))
        return self.list_of_lists

    def punctuation(self):
        '''
        Removes all non numerical/alphabetical characters
        :return: Returns a list of lists with no punctuation and no empty values
        '''
        num_doc = len(self.list_of_lists)
        for i in range(num_doc):
            current_list = self.list_of_lists[i]
            for idx, each_word in enumerate(current_list):
                current_list[idx] = re.sub('[^a-zA-Z0-9]+', '', each_word)
            current_list = list(filter(None, current_list))
            self.lol_no_punc.append(current_list)
        return self.lol_no_punc

    def singular(self):
        '''
        Tries to remove plural words and make them singular
        :return: Returns a list of lists with no plural words
        '''
        p = inflect.engine()
        for each_list in self.lol_no_punc:
            current_list = each_list
            for idx, each_word in enumerate(current_list):
                singular = p.singular_noun(each_word)
                if singular is False:
                    current_list[idx] = each_word.lower()
                elif singular is not False:
                    current_list[idx] = singular.lower()
            self.lol_no_plural.append(current_list)
        return self.lol_no_plural

    def word_dict(self):
        '''
        Returns a dictionary where the 'key' is a word. Using indexing, you can access the count of the word in
        each document.
        :return: A hash table of words
        '''
        num_doc = len(self.lol_no_plural)

        for idx, current_list in enumerate(self.lol_no_plural):
            for current_word in current_list:
                if current_word not in self.hash_table:
                    self.hash_table[current_word] = [Counter() for i in range(num_doc)]
                    self.hash_table[current_word][idx].update([current_word])
                elif current_word in self.hash_table:
                    self.hash_table[current_word][idx].update([current_word])
        return self.hash_table
