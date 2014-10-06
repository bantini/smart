import os
from gensim import corpora,models,similarities
from os.path import join
import SpecialEntityRemover as se
import LSI

def varietyProcessor():
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    write_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
    lsi_model = LSI.lsi("ukr.txt")
    with open(join(verify_path,'ukr_out.txt'),'r') as reader,open(join(write_path,'ukr_verified.csv'),'w') as writer:
        for line in reader:
            try:
                line = line.split(',')
                line = ",".join(line[1:]).encode('UTF-8')
                vec_bow = dictionary.doc2bow(se.pattern_matcher(line))
                vector_lsi = lsi[vec_bow]
                print "%s:%s"%(str(vector_lsi[1][1]),document)
                writer.write("%s:%s"%(str(vector_lsi[1][1]),document))
            except IndexError:
                pass

