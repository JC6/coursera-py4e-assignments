import ssl
import urllib.request

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i = 0
while i < count - 1:
    tags = soup('a')
    html = urllib.request.urlopen(tags[position - 1].get('href', None), context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    i += 1
print(soup('a')[position - 1].contents[0])
