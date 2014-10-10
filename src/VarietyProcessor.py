__author__ = 'nilayan'

import os
import SpecialEntityRemover as se
from os.path import join
import LSI as lsi
def varietyProcessor():
    #initial_query = set(['ukraine'])
    #expanded_query = set(['russia','putin','obama','crimea','palin'])
    lsi_model,dictionary = lsi.lsi("ukr.txt")
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    output_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
    with open(join(verify_path,'ukr.txt'),'r') as reader,open(join(output_path,'ukr_expt2.csv'),'w') as writer:
        for line in reader:
            initial = 0
            russia = 0
            obama = 0
            crimea = 0
            palin = 0
            line = set(se.pattern_matcher(line.rstrip().split()))
            line_bow = dictionary.doc2bow(line)
            lsi_output = lsi_model[line_bow]
            if 'ukraine' in line:
                initial+=1
            if 'russia' in line:
                russia+=1
            if 'obama' in line:
                obama+=1
            if 'crimea' in line:
                crimea+=1
            if 'palin' in line:
                palin+=1
            try:
                print "Ukraine:%d,Russia:%d,Obama:%d,Crimea:%d,Palin:%d,LSi Score:%s"%(initial,russia,obama,crimea,palin,lsi_output[0][1])
                writer.write("%d,%d,%d,%d,%d,%f\n"%(initial,russia,obama,crimea,palin,lsi_output[0][1]))
            except IndexError:
                print "Ukraine:%d,Russia:%d,Obama:%d,Crimea:%d,Palin:%d,LSi Score:0.0"%(initial,russia,obama,crimea,palin)
                writer.write("%d,%d,%d,%d,%d,0.0\n"%(initial,russia,obama,crimea,palin))
    #print "Ukraine:%d,Russia:%d,Obama:%d,Crimea:%d,Palin:%d"%(initial,russia,obama,crimea,palin)

def main():
    varietyProcessor()

if __name__=='__main__':
    main()



