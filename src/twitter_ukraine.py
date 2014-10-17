from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
from time import gmtime,strftime
import json
import logging

from os.path import join
ckey='ThjLwQWrklaEBAKwf5WaGg'
csecret='ZbAY5mywkqPlCQJFQSX5gavJj7CIK52JuU596yOtnw'
atoken='141498497-6XCX1AXlurKhPAB1wm4TPbxG77p3pMWajzrU0ewG'
asecret='zqNzPPreO3ALJ5UrZj6okNw6aDg5pZE4r1U7y2ujE'
start_time = None

class listener(StreamListener):
	counter = 0	
	def on_data(self,data):
		try:
			print listener.counter 	
			#start_time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
			logging.basicConfig(filename='ukraine_velocity.log',format = '%(asctime)-15s %(message)s',level=logging.INFO)
			if listener.counter == 100:
				logging.info("Counter reset")
				listener.counter = 0
			elif listener.counter ==0:
				logging.info("Counter start")
			listener.counter+=1
			dirty = open('ukraine_velocity2.txt','a')
			encoded = data.encode('UTF-8')
			dirty.write(encoded)
			dirty.write('\n')
			dirty.close()
			json_data = json.loads(encoded)
			tweet = json_data["text"]
			#tweet = data.split(',"text":"')[1].split('","source')[0]
			#print tweet
			#saveThis = str(time.time())+'::'+tweet
			saveFile = open('ukraine_velocity_clean2.txt','a')
			saveFile.write(tweet.encode("UTF-8"))
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(5)
	def on_error(self, status):
		print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track = ['ukraine','russia','kiev','euromaidan','obama'])

