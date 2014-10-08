__author__ = 'nilayan'

import os
import SpecialEntityRemover as se
from os.path import join
def varietyProcessor():
    #initial_query = set(['ukraine'])
    #expanded_query = set(['russia','putin','obama','crimea','palin'])
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    initial = 0
    russia = 0
    obama = 0
    crimea = 0
    palin = 0
    with open(join(verify_path,'ukr.txt'),'r') as reader:
        for line in reader:
            line = set(se.pattern_matcher(line.rstrip().split()))
            if 'ukraine' in line:
                initial+=1
            else:
                if 'russia' in line:
                    russia+=1
                if 'obama' in line:
                    obama+=1
                if 'crimea' in line:
                    crimea+=1
                if 'palin' in line:
                    palin+=1
    print "Ukraine:%d,Russia:%d,Obama:%d,Crimea:%d,Palin:%d"%(initial,russia,obama,crimea,palin)

def main():
    varietyProcessor()

if __name__=='__main__':
    main()



