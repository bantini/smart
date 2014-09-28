import gzip
import os
from os.path import join
__author__ = 'nilayan'

corpus_path = path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))

file = gzip.open(join(corpus_path,"syria_full.txt.gz"),"r")
for line in file:
    print line