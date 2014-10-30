import gzip
import os
from os.path import join
import json
import time
__author__ = 'nilayan'

corpus_path = path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
unique_counter = 0
found_counter = 0
total = 0
listOfId = {}
file = gzip.open(join(corpus_path,"syria_velocity1.txt.gz"),"r")
writer = open(join(corpus_path,"syr_vel1.txt"),'w')
for line in file:
    if len(line.strip()) >0:
        total+=1
        try:
            json_data = json.loads(line)
            #time.sleep(1)
            try:
                t_id = json_data["retweeted_status"]["id"]
                #print t_id
                if t_id in listOfId:
                    found_counter+=1
                    pass
                else:
                    text = json_data["retweeted_status"]["text"]
                    #print text
                    text = text.encode("UTF-8")
                    # created_at = json_data["retweeted_status"]["created_at"]
                    ts = time.strftime('%Y-%m-%d %H:%M:%S',
                                   time.strptime(json_data["retweeted_status"]["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))
                    #tweetObject = Tweet(text,created_at)
                    #print "%s,%s\n" % (ts, text)
                    writer.write("%s,%s\n" % (ts, text))
                    unique_counter+=1
                    listOfId[t_id] = True
            except KeyError:
                text = json_data["text"]
                #print text
                ts = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(json_data["created_at"], '%a %b %d %H:%M:%S +0000 %Y'))
                text = text.encode("UTF-8")
                #print text
                try:
                    t_id = json_data["id"]
                    #print t_id
                    if t_id in listOfId:
                        found_counter+=1
                        pass
                    else:
                        listOfId[t_id] = True
                        unique_counter+=1
                        writer.write("%s,%s\n" % (ts, text))
                        #print "Written:"+text
                except Exception, e:
                    print "Inner loop exception:"
                    pass
        except Exception, e:
            pass

print "%d,%d,%d"%(unique_counter,found_counter,total)