# may later need to url encode to RFC 1738
# from urlparse import urlparse 

import base64
import urllib
import urllib2
import json

consumer_key='TJDOq5D2tC4VognfhCMy6w'
consumer_secret='KNvhZxfCZkfdBnrqVdz18mnRoMe6JJLeO5Wl0P1wkk'

credentials = consumer_key + ':' + consumer_secret
encodedcred = base64.urlsafe_b64encode(credentials)

url = "https://api.twitter.com/oauth2/token"

data = {'Authorization' : 'Basic ' + encodedcred,
	  'User-Agent' : 'njclassifier',
          'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8',
          'Content-Length' : '29',
	  }


value = {'grant_type' : 'client_credentials'}

valueEnc = urllib.urlencode(value)


try:
    req = urllib2.Request(url, valueEnc, data)
    response = urllib2.urlopen(req)
    content = response.read()
    
    
except Exception, e:
   print e






