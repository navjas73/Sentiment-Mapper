from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os, sys
import json
import datetime
import sqlite3

infile = open('keys.txt', 'r')

consumer_key= (infile.readline()).rstrip('\n')
consumer_secret= (infile.readline()).rstrip('\n')
access_token= (infile.readline()).rstrip('\n')
access_token_secret= (infile.readline()).rstrip('\n')

infile.close()

DATABASE_NAME = "test.db"

#Listens to stream, decides what to do with it
class StdOutListener(StreamListener):

    # If transmitted tweet is received correctly
    def on_data(self, data):
	print data	
	return True

    # if there was an error
    def on_error(self, status):
	# for now, dont stop the stream
        print status	
	return True

    # if timeout from tweet stream
    def on_timeout(self):
	# for now, dont stop the stream
	print 'Timed out....'
	return True


# Class for tweet stream
class streamsample(StreamListener): 
   
    # constructor for stream
    def __init__(self):
       l = StdOutListener() 
       auth = OAuthHandler(consumer_key, consumer_secret)
       auth.set_access_token(access_token, access_token_secret) 
       self.stream = Stream(auth, l)    

    def printtest(self):
	self.stream.sample()
	
    # Sends tweet to the sqlite3 database
    def todatabase(self, numtweets = 100):
	
	connection = sqlite3.connect(DATABASE_NAME)
	cursor = connection.cursor()

	try:
	    count = 0
	    while count < numtweets:
		for tweet_json in self.stream:
		    #check whether the tweet is actually a tweet
		    if tweet.get('text') and tweet['user']['lang'] == 'en':
			parsetweet(tweet_json)
		    break
		count += 1

	except stream.ConnectionError, e:
	    print "Disconnected"

    
    def parsetweet(self, tweet_json):
	tweet = json.loads(tweet_json)
	
	id = tweet["id"]
	created_at = datetime.datetime(*rfc822.parsedate(tweet["created_at"])[:6])
	text = tweet["text"]

	#if tweet["user"]["geo_enabled"] == True or tweet["user"]["geo_enabled"] == "true"
	    
s = streamsample()
s.printtest()
