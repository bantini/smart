import requests
import time
from os.path import join
import json

#Use the spotlight API to identify the entities

def spotlightCaller():
    path = "/Users/nilayan/Project/data"
    url = "http://spotlight.dbpedia.org/rest/annotate?text="
    #url = 'http://lookup.dbpedia.org/api/search/KeywordSearch?QueryClass=place,person&QueryString='
    tail = "&types=Person,Organization,Place,Country"
    header = {"Accept": "application/json"}
    items = ['russia', 'putin', 'crimea', 'obama', 'palin']
    for item in items:
        response = requests.get(url+item+tail, headers=header)
        json_data = json.loads(response.text)
        print json_data
        #print text
        #types = data["annotation"]["surfaceForm"]["resource"]["types"]
        #print types


def main():
    spotlightCaller()


if __name__ == "__main__":
    main()
