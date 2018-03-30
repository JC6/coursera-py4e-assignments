import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
comments_sum = 0
for tag in tags:
    comments_sum += int(tag.contents[0])
print("Count ", len(tags))
print("Sum ", comments_sum)
