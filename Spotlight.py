import requests
import time
from os.path import join

def spotlightCaller():
	path = "/Users/nilayan/Project/data"
	url = "http://spotlight.dbpedia.org/rest/annotate?text="
	header = {"Accept":"application/json"}
	response = requests.get(url+"Barack+Obama",headers=header)
	print response.text
	"""
	with open(join(path,"tweets.txt"),"r") as w:
		temp = 0
		for line in w:
			if temp>100:
				break
			else:
				response = requests.get(url+line,headers=header)
				print response.text
				temp+=1
				time.sleep(5)
	"""
def main():
	spotlightCaller()

if __name__=="__main__":
	main() 
