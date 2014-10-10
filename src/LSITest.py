from gensim import corpora,models,similarities
import LSI as lsi
import SpecialEntityRemover as se
import os
from os.path import join
__author__ = 'nilayan'

def test1():
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    with open(join(path,"ukr.txt"),"r") as reader:
        for line in reader:
            line = line.split(',')
            line = ' '.join(line[1:])
            line = line.split()
            temp = se.pattern_matcher(line[1:])
            if len(temp)>0:
                print temp

def main():
    test1()

if __name__=="__main__":
    main()


