__author__ = 'nilayan'

import os
import SpecialEntityRemover as se
from os.path import join
import LSI as lsi
def varietyProcessor():
    #initial_query = set(['ukraine'])
    #expanded_query = set(['russia','putin','obama','crimea','palin'])
    lsi_model,dictionary = lsi.lsi("war_1.txt")
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    output_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
    with open(join(verify_path,'ukr_v2.txt'),'r') as reader,open(join(output_path,'ukr_1_4.csv'),'w') as writer:
        counter  = 1
        for line in reader:
            counter+=1
            #Replace kiev, euromaidan with kiev and palin
            initial = 0
            russia = 0
            obama = 0
            crimea = 0
            palin = 0
            line = set(se.pattern_matcher(line.rstrip().split()))
            line_bow = dictionary.doc2bow(list(line))
            lsi_output = lsi_model[line_bow]
            if 'ukraine' in line:
                initial+=1
            if 'russia' in line:
                russia+=1
            if 'obama' in line:
                obama+=1
            if 'kiev' in line:
                crimea+=1
            if 'euromaidan' in line:
                palin+=1
            try:
                writer.write("%d,%d,%d,%d,%d,%f\n"%(initial,russia,obama,crimea,palin,lsi_output[1][1]))
            except IndexError:
                writer.write("%d,%d,%d,%d,%d,0.0\n"%(initial,russia,obama,crimea,palin))
    print counter

def main():
    varietyProcessor()

if __name__=='__main__':
    main()



