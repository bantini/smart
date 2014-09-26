#with code generously borrowed from gensim

import logging
import NE
import csv
from collections import defaultdict
from gensim import corpora,models,similarities
from os.path import join 

def stopWordReader(f):
	listOfStopWords = defaultdict()
	with open(join("../input",f),"r") as r:
		for line in r:
			line = line.lstrip().rstrip()
			#print line
			listOfStopWords[line] = True
	return listOfStopWords


def dictionaryCreator(tweets):
	dictionary = corpora.Dictionary(tweets)
	dictionary.save("../dicts/ukraine_1m2_5.dict")
	return dictionary

def lsi():
	logging.basicConfig(file = "../log/u_1m2_5_out.log",format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	documents = []
	f = "englishST.txt"
	stopWords = stopWordReader(f)
	with open(join("../input","ukr_50k.txt"),"r") as reader:
		csv_reader = csv.reader(reader)
		for row in reader:
			line = row[1]
			print line
			if len(line)>1:
				print line
				documents.append(line)
				#documents.append(NE.namedEntityExtractor(line))
	tweets = [[word for word in document.lower().split() if word not in stopWords]for document in documents]
	dictionary = dictionaryCreator(tweets)
	#dictionary = dictionaryCreator(documents)
	corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
	#corpus = [dictionary.doc2bow(document) for document in documents]
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]
	corpora.MmCorpus.serialize("../corpus/tweetcorpus_1m2_5.mm",corpus)
	lsi = models.LsiModel(corpus_tfidf,id2word = dictionary,num_topics = 5)
	lsi.print_topics(2)
	#print lsi
#def main():
	
			
#if __name__=="__main__":
#	main()
		
