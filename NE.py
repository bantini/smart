import nltk
import re
from os.path import join

def namedEntityExtractor(sentence):
	tokenized = nltk.word_tokenize(sentence)
	tagged = nltk.pos_tag(tokenized)
	namedEntity = nltk.ne_chunk(tagged,binary=True)
	compiler = re.compile("[(]['][a-zA-Z]+[']")
	listOfWords = []
	for chunks in namedEntity:
		#print chunks[0]
		if compiler.match(str(chunks[0])):
			chunk = str(chunks[0])
			front = chunk[2:]
			word = re.search("[a-zA-Z]+[']",front)
			#print word.group(0)[:-1]
			listOfWords.append(word.group(0)[:-1])
	return listOfWords

def main():
	path = "/Users/nilayan/Project/data"
	with open(join(path,"palestine_tweets.txt"),"r") as reader:
		for line in reader:
			namedEntityExtractor(line)

if __name__=="__main__":
	main()