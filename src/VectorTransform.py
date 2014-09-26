import logging
from gensim import corpora, models, similarities

class VectorTransform:
	def __init__(self,tweets):
		
