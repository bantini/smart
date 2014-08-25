import json
from os.path import join
from collections import defaultdict

class Tweet:
	def __init__(self, text, created_at):
		self.text = text
		self.created_at = created_at

def tweetReader(f):
	listOfId = defaultdict(long)
	path = "/Users/nilayan/Downloads/D"
	with open(join(path,f),"r") as r:
		counter = 0
		for line in r:
			#print line
			try:
				json_data = json.loads(line)
				try:
					id = json_data["retweeted_status"]["id"]
					if listOfId[id]:
						pass
					else:
						text = json_data["retweeted_status"]["text"]
						created_at = json_data["retweeted_status"]["created_at"]
						tweetObject = Tweet(text,created_at)
						with open(join(path,"palestine_tweets.txt"),"a") as w:
							w.write("%s\n"%(text))
						listOfId[id] = tweetObject
						if counter>50000:
							print counter
							break
						else:
							print "Old"
							print counter
							counter+=1
				except KeyError:
					text = json_data["text"]
					try:
						id = json_data["id"]
						if listOfId[id]:
							pass
						else:
							with open(join(path,"palestine_tweets.txt"),"a") as w:
                                                        	w.write("%s\n"%(text))
						created_at = json_data["created_at"]
						tweetObject = Tweet(text,created_at)
						if counter>50000:
							print "New"
							print counter
							break
						else:
							print "New"
							print counter
							counter+=1
					except Exception,e:
						print "Inner loop exception:"
						print e
						pass
			except Exception,e:
				print "Outer loop exception"
				print e
				pass

def main():
	f = "palestine_full.txt"
	tweetReader(f)

if __name__ == "__main__":
	main()
	
			
