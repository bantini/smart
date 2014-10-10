import os
from gensim import corpora,models,similarities
from os.path import join
import SpecialEntityRemover as se
import LSI

def lsiProcessor():
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    write_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
    lsi_model,dictionary = LSI.lsi("ukr.txt")
    with open(join(verify_path,'ukr_out.txt'),'r') as reader,open(join(write_path,'ukr_verified.csv'),'w') as writer:
        for line in reader:
            try:
                #print "Line:%s"%line
                tweet = line.split(':')
                tweet = ":".join(tweet[1:])
                tweet = se.pattern_matcher(tweet.split())
                if len(tweet)>0:
                    vec_bow = dictionary.doc2bow(se.pattern_matcher(tweet))
                    vector_lsi = lsi_model[vec_bow]
                    print "%s:%s"%(str(vector_lsi[1][1]),line)
                #writer.write("%s:%s"%(str(vector_lsi[1][1]),line))
            except IndexError:
                pass

