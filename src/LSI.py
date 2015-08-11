#with code generously borrowed from gensim
import logging
import os
import gzip
from collections import defaultdict
from gensim import corpora,models,similarities
from os.path import join
import SpecialEntityRemover as se

#Use the LSI algorithm on the tweets file 'f'

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
    #path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'dicts'))
    #dictionary.save(join(path,"ukr_50k.dict"))
    return dictionary

def lsi(f):
    path_log = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'log'))
    file_log = join(path_log,f+".log")
    path_model = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'dicts'))
    file_model = join(path_model,f+".lsi")
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    logging.basicConfig(filename = file_log,format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    min_time = None
    max_time = None
    documents = []
    with open(join(path, f),"r") as reader:
        #csv_reader = csv.reader(reader)
        for row in reader:
            try:
                import time
                time_file = row.split(",")[0]
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
                if len(line)>1:
                    documents.append(line)
            except IndexError:
                pass
            except Exception, e:
                print e
                print row
                pass
    logging.info("Min-time:%s",min_time)
    logging.info("Max-time:%s",max_time)
    tweets = [[word for word in se.pattern_matcher(document.lower().split())]for document in documents[:1000]]
    dictionary = dictionaryCreator(tweets)
    corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    #corpus_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'corpus'))
    #corpora.MmCorpus.serialize(join(corpus_path, "ukr_50k.mm"),corpus)
    lsi = models.LsiModel(corpus_tfidf,id2word = dictionary,num_topics = 2)
    #lsi.save(file_model)
    lsi.print_topics(2,10)
    print "Showing topics"
    topics = lsi.show_topics()
    for topic in topics:
            print topic
    return lsi,dictionary
