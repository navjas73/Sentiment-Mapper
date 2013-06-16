import json, urllib, urllib2

twid = '125082707389718529'
bearer = 

url = 'https://api.twitter.com/1.1/statuses/show.json?id=' + twid

header = {'Authorization' : 'Bearer ' + bearer,
	  'User-Agent' : 'njclassifier'
	  }

try:
    req = urllib2.Request(url, None, header)
    response = urllib2.urlopen(req)
    content = response.read()
    print content
except Exception, e:
   print e
