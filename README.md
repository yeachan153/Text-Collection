# Text-Collection

The aim of this project is to read in a semi-structured file ('txt for-assignment-data-science.text'), and create a hash table. The current file contains 3 articles from the LA Times articles collection. 

The hash-table's purpose is to count the number of times that a word appears in each article. For example, entering the word as a 'key' to the hash table will bring up a list of counters that are indexed in order of document number. The only thing to take into consideration is zero-indexing. Thus, to find out how many times 'and' would appear in document number 1, type 'hashtable['and'][0]'. This accesses the counter in the first element of the list.

The repository contains 3 relevant files:
- TextCollect.py
    - This contains the class TextCollect() which contains methods that are used. Tags in the file e.g. '\</p>' that mark the documents are removed. Punctuation is also removed by removing all non alphabetical or numerical values. Finally, words are also singularised and lower-cased to avoid multiple counts for similar words, e.g. 'cow', 'cows'.
- txt-for-assignment-data-science.txt
    - This contains the raw semi-structured data.
- Text Collection - Demo and Visualisation.ipynb
    - This contains the demonstration of how to use the class, and plots a histogram of the number of times a word appeared in all documents.