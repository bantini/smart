from _ast import operator

__author__ = 'nilayan'
from os.path import join
import json
import operator
hash_tag_dict = {}
def hashTagExtractor():
    file_name = "/home/nilayan/Thesis/smart/src/war_2_json.txt"
    with open(file_name,'r') as reader:
        for line in reader:
            try:
                tweet = json.loads(line)
                hash_tags = tweet['entities']['hashtags']
                if len(hash_tags)>0:
                    for tag in hash_tags:
                        hash_tag =  tag['text']
                        hash_tag = hash_tag.encode('UTF-8')
                        try:
                            temp = hash_tag_dict[hash_tag]
                            temp+=1
                            hash_tag_dict[hash_tag] = temp
                        except KeyError:
                            hash_tag_dict[hash_tag] = 1
            except KeyError:
                pass
            except ValueError:
                print line
    sorted_items = sorted(hash_tag_dict.items(),key=operator.itemgetter(1),reverse=True)
    print sorted_items[1:10]
def main():
    hashTagExtractor()

if __name__=="__main__":
    main()