import urllib2
import xml.etree.ElementTree as ET




(lat, lon) = (47.64054,-122.12934)

latstr = str(lat)
lonstr = str(lon)


url = 'http://dev.virtualearth.net/REST/v1/Locations/' + latstr + ',' + lonstr + '?o=xml&key=AgqN2WGsxDmLMM6vJUWctW5kRLkgNcMjYJ7iuf2rRy27mwjOQh1mU8oi9VDMIEsj'




try:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    content = response.read()          
    root = ET.fromstring(content)
    code = root[6][0][1][0][4][6]
    
    print code.text

except Exception, e:
    print e
