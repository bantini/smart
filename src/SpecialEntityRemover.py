from curses.ascii import isalpha

__author__ = 'nilayan'

import re
import logging
import os
from os.path import join
from collections import defaultdict

def stopWordReader(f):
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    list_of_stop_words = defaultdict()
    with open(join(path,f),"r") as r:
        for line in r:
            line = line.lstrip().rstrip()
            #print line
            list_of_stop_words[line] = True
    return list_of_stop_words

def pattern_matcher(items):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    documents = []
    f = "englishST.txt"
    stopWords = stopWordReader(f)
    hash_pattern = re.compile('[#][a-zA-Z0-9]+')
    user_pattern = re.compile('[@][a-zA-Z0-9]+')
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    cleaned_items = []
    for item in items:
        if re.match(hash_pattern,item.lower()):
            word = item.lower()[1:]
            word = ''.join(e for e in word if e.isalpha())
            if len(word.lstrip().rstrip())>0:
                cleaned_items.append(word)
        elif re.match(user_pattern,item.lower()):
            pass
        elif re.match(url_pattern,item.lower()):
            pass
        elif item.lower() in stopWords:
            pass
        else:
            item = ''.join(e for e in item if e.isalpha())
            if len(item.lstrip().rstrip())>0:
                cleaned_items.append(item.lower())
    return cleaned_items

