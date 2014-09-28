from gensim import corpora,models,similarities
__author__ = 'nilayan'

dictionary = corpora.Dictionary(None)
corpus = dictionary.doc2bow(None)
tfidf_model  = models.TfidfModel(corpus)
corpus = tfidf_model[corpus]
corpora.MmCorpus.serialize(corpus)
lsi = models.LsiModel.

