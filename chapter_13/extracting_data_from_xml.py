import urllib.request
import xml.etree.ElementTree as ElementTree

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ElementTree.fromstring(data)
counts = tree.findall('.//count')
count_sum = 0
for count in counts:
    count_sum += int(count.text)
print('Count:', len(counts))
print('Sum:', count_sum)
