import json
import time
<<<<<<< HEAD
=======
import gzip
>>>>>>> 3dbb5d07c510bda42e8917907f8249b97458fc3d
import os
from os.path import join
from collections import defaultdict

class Tweet:
	def __init__(self, text, created_at):
		self.text = text
		self.created_at = created_at

def tweetReader(f):
	listOfId = defaultdict(long)
<<<<<<< HEAD
	path = path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
	with open(join(path,f),"r") as r:
		counter = 0
		out_file = "ukr_new.txt"
=======
	path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
	with gzip.open(join(path,f),"r") as r:
		counter = 0
		out_file = "isr.txt"
>>>>>>> 3dbb5d07c510bda42e8917907f8249b97458fc3d
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
						text = text.encode("UTF-8")
						#created_at = json_data["retweeted_status"]["created_at"]
						ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(json_data["retweeted_status"]["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))	
						#tweetObject = Tweet(text,created_at)
						with open(join(path,out_file),"a") as w:
							print "%s,%s\n"%(ts,text)
							w.write("%s,%s\n"%(ts,text))
							listOfId[id] = True
				except KeyError:
					text = json_data["text"]
					ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(json_data["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))
					text = text.encode("UTF-8")
					try:
						_id = json_data["id"]
						if listOfId[id]:
							pass
						else:
							listOfId[id] = True
							with open(join(path,out_file),"a") as w:
								w.write("%s,%s\n"%(ts,text))
					except Exception,e:
						print "Inner loop exception:"
						print e
						pass
			except Exception,e:
				print "Outer loop exception"
				print e
				pass

def main():
<<<<<<< HEAD
	f = "ukraine_new.txt"
=======
	f = "israel_full.txt.gz"
>>>>>>> 3dbb5d07c510bda42e8917907f8249b97458fc3d
	tweetReader(f)

if __name__ == "__main__":
	main()
	
			
