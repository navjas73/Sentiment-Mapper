import csv, json, urllib, os
import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getTweet(searchstring):
   
    # stay within rate limits
    max_tweets_per_hr  = 300
	
    # download tweets
    for idx in range(0,10):

        # pull data
        url = 'https://api.twitter.com/1.1/search/tweets.json?q=%40' + searchstring
        urllib.urlretrieve( url, raw_dir + item[2] + '.json' )

        # stay in Twitter API rate limits 
        print '    pausing %d sec to obey Twitter API rate limits' % \
              (download_pause_sec)
        time.sleep( download_pause_sec )

    return

