import tweepy
import os, sys
import json
consumer_key="zYALdBBc17mdKnUc60mtoA"
consumer_secret="1WCVlmevtZ3rIlVLgA5zp2BELkY3WSd23BQfy3CysI"
access_token=
access_token_secret=

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Construct the API instance
api = tweepy.API(auth)

tweets=api.get_status(126415614616154000)
print tweets
