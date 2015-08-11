__author__ = 'nilayan'

import os
import sys
import SpecialEntityRemover as se
from os.path import join
import re
import csv

#Open the tweets file in 'reader', search for the search queries in 'terms' and write it in the form of a csv in 'writer'
def varietyProcessor():
    terms = ['uga','Dawgs','UF','GAFL14','FLGA14','GoDawgs','Georgia','UGAvsUF','bulldogs','ItsTime','UFvsUGA','Gators','Zelo','Florida','ItsGreatUF','GatorNation','GoGators']
    terms_clean = [term.lower() for term in terms]
    no_of_terms = len(terms_clean)
    output_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
    input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    hash_pattern = re.compile('[#][a-zA-Z0-9]+')
    with open(join(input_path,'uga_7_clean.txt'),'r') as reader,open(join(output_path,'uga_out_7.csv'),'w') as writer:
        csv_writer = csv.writer(writer)
        for line in reader:
            search_terms = [0]*no_of_terms
            words = line.split()
            for word in words:
                word = word.lower()
                if re.match(hash_pattern,word):
                    word = word.lower()[1:]
                    word = ''.join(c for c in word)
                try:
                    i = terms_clean.index(word)
                    search_terms[i] = 1
                except ValueError:
                    pass
                except KeyError:
                    pass
            csv_writer.writerow(search_terms)


def main():
    varietyProcessor()

if __name__=='__main__':
    main()



