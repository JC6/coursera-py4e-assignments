import json
import urllib.request

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('User count:', len(info))
count_sum = 0
for item in info['comments']:
    count_sum += int(item['count'])
print('Count:', len(info['comments']))
print('Sum:', count_sum)
