import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
lst = list()
for tag in tags:
    n = tag.string #https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/
#    print(n)
    n = int(n) #it is ok to use the same varieble when converting to integer
#    print(N)
    lst.append(n)
print(sum(lst))
