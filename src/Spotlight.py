import requests
import time
from os.path import join


def spotlightCaller():
	path = "/Users/nilayan/Project/data"
	url = "http://spotlight.dbpedia.org/rest/annotate?text="
	header = {"Accept":"application/json"}
	items = ['russia','putin','crimea','obama','palin']
	for item in items:
		response = requests.get(url+item,headers=header)
		print response.text

def main():
	spotlightCaller()

if __name__=="__main__":
	main() 
