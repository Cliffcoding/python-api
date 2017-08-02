import json
import urllib2

url = "http://127.0.0.1:5000/api/song/1"

data = json.load(urllib2.urlopen(url))

print data[2]
