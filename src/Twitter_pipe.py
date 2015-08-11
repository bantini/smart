from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import RotatingFile
from os.path import join
import argparse


#Start collecting tweets. The usage is python Twitter_pipe.py -s <search_term>
class listener(StreamListener):
	passed_filename = "test"
	def __init__(self,filename):
		listener.passed_filename = filename
	def on_data(self,data):
		try:
			print listener.passed_filename
			path = "../data/"
			encode = data.encode('UTF-8')
			json_data = json.loads(encode)
			tweet = json_data["text"]
			tweet = tweet.encode("UTF-8")
			print tweet
			"""
			twitter_file = RotatingFile(directory = path,search_term = listener.passed_filename)
			while not twitter_file.finished:
				twitter_file.write(tweet)
			"""
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(5)

	def on_error(self, status):
		print "Error error error"
		print status
		if status == 420:
			print "Yippie:caught error!!!"
			time.sleep(60)

class fileListener(listener):
	def __init__(self,filename):
		self.filename = filename


def main():
	ckey='J1YIskl5lCtCerXGGCUjMWBQE'
	csecret='Ua0GwKXh0l2oCjp61ApuiZrbhrnR2g7PwReqf8XZu8sEsMTAEj'
	atoken='2411733278-knx8uVxgOmSvyk8gbPaNs8EJM1G1cB41zvii5lg'
	asecret='PdG9SqxTvENZW5RbTfBD81JMU3QZUfaFdHny3GGxEv4WB'
	parser = argparse.ArgumentParser(description="The search term to be queried")
	parser.add_argument("--search","-s",help = "Search term to query twitter with")
	search = parser.parse_args()
	filename = "%s_%s"%(search.search,str(time.time()).replace(".",""))
	#print filename
	auth = OAuthHandler(ckey,csecret)
	auth.set_access_token(atoken,asecret)
	twitterStream = Stream(auth,listener(search.search))
	#print search.search
	twitterStream.filter(track = [search.search])


if __name__=="__main__":
	main()

