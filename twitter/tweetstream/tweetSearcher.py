import sqlite3
import urllib2
#conn = sqlite3.connect('tweetdb.db')
#c = conn.cursor()

#c.execute('''CREATE TABLE tweets
		#(User, Text, Location)''')


keyword = raw_input('Enter keyword: ')

 # pull data
	
url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + keyword
bearer = 'AAAAAAAAAAAAAAAAAAAAAJZ6RQAAAAAAI4OPhfJoxxZwb1VpIW7etxloDGM%3D3N0xImBkV8sykZHTXdzRRUPhd9Xx7SKlttTUFoHTA'	
header = {'Authorization' : 'Bearer ' + bearer, 'User-Agent' : 'njclassifier'}

try:
    req = urllib2.Request(url, None, header)
    response = urllib2.urlopen(req)
    content = response.read()          
    print content
    	    
except Exception, e:
    print e
