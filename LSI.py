#with code generously borrowed from gensim

import logging
from collections import defaultdict
from gensim import corpora,models,similarities
from os.path import join 

def stopWordReader(f,path):
	listOfStopWords = defaultdict()
	with open(join(path,f),"r") as r:
		for line in r:
			line = line.lstrip().rstrip()
			#print line
			listOfStopWords[line] = True
	return listOfStopWords


def dictionaryCreator(tweets):
	dictionary = corpora.Dictionary(tweets)
	dictionary.save("/Users/nilayan/Project/data/palestine.dict")
	return dictionary

def lsi():
	logging.basicConfig(filename = "palestine_out.log",format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	documents = []
	path = "/Users/nilayan/Project/data"
	f = "englishST.txt"
	stopWords = stopWordReader(f,path)	
	with open(join(path,"palestine_tweets.txt"),"r") as reader:
		for line in reader:
			if len(line)>1:
				documents.append(line)
	tweets = [[word for word in document.lower().split() if word not in stopWords]for document in documents]
	dictionary = dictionaryCreator(tweets)
	corpus = [dictionary.doc2bow(tweet) for tweet in tweets]
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]
	corpora.MmCorpus.serialize("/Users/nilayan/Project/data/tweetcorpus.mm",corpus)
	lsi = models.LsiModel(corpus_tfidf,id2word = dictionary,num_topics = 2)
	#lsi.print_topics(2)
	print lsi
#def main():
	
			
#if __name__=="__main__":
#	main()
		
