#with code generously borrowed from gensim
import logging
import os
import gzip
from collections import defaultdict
from gensim import corpora,models,similarities
from os.path import join
import SpecialEntityRemover as se

def stopWordReader(f):
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    list_of_stop_words = defaultdict()
    with open(join(path,f),"r") as r:
        for line in r:
            line = line.lstrip().rstrip()
            #print line
            list_of_stop_words[line] = True
    return list_of_stop_words


def dictionaryCreator(tweets):
    dictionary = corpora.Dictionary(tweets)
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'dicts'))
    dictionary.save(join(path,"ukr_50k.dict"))
    return dictionary

def lsi():
    path_log = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'log'))
    file_log = join(path_log,"ukr_50k.log")
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    documents = []
    f = "englishST.txt"
    stopWords = stopWordReader(f)
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    min_time = None
    max_time = None
    with open(join(path, 'ukr.txt'),"r") as reader:
        #csv_reader = csv.reader(reader)
        for row in reader:
            try:
                import time
                time_file = row.split(",")[0]
                #ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(time_file,'%Y-%m-%d %H:%M:%S'))
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(time_file,'%Y-%m-%d %H:%M:%S'))
                if min_time is None:
                    min_time = ts
                else:
                    if ts<min_time:
                        min_time = ts
                if max_time is None:
                    max_time = ts
                else:
                    if ts>max_time:
                        max_time = ts
            except ValueError:
                pass
            try:
                row = row.split(",")
                time = row[1]
                line = ",".join(row[1:])
                #print line
                if len(line)>1:
                    #print line
                    documents.append(line)
            except IndexError:
                pass
            except Exception, e:
                print e
                print row
                pass


            #documents.append(NE.namedEntityExtractor(line))
    logging.info("Min-time:%s",min_time)
    logging.info("Max-time:%s",max_time)
    tweets = [[word for word in se.pattern_matcher(document.lower().split()) if word not in stopWords]for document in documents[:50000]]
    dictionary = dictionaryCreator(tweets)
    #dictionary = dictionaryCreator(documents)
    corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
    #corpus = [dictionary.doc2bow(document) for document in documents]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    corpus_path = path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'corpus'))
    corpora.MmCorpus.serialize(join(corpus_path, "ukr_50k.mm"),corpus)
    #lsi = models.LsiModel(corpus_tfidf,id2word = dictionary,num_topics = 2)
    #lsi.show_topics()
    lsi = models.LsiModel(corpus_tfidf,id2word = dictionary,num_topics = 2)
    """
    for document in documents:
        try:
            path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
            with open(join(path,"ukr_out_2.txt"),"a") as writer:
                vec_bow = dictionary.doc2bow(se.pattern_matcher(document.lower().split()))
                vector_lsi = lsi[vec_bow]
                print "%s:%s"%(str(vector_lsi[1][1]),document)
                writer.write("%s:%s"%(str(vector_lsi[1][1]),document))
        except IndexError:
            pass
    """
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    write_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
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



    #print lsi
#def main():


#if __name__=="__main__":
#	main()

