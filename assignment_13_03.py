import json
import urllib.request, urllib.parse

service_url = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
url = service_url + urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
print('Place id ' + js['results'][0]['place_id'])
