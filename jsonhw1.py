#某人寫出了API，我們依照API的json的格式去寫程式，以便找出我們要的tag，並取出資料。
import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
lst = list()
#print(html)
info = json.loads(html) #info是將html轉成dictionary，有時或許是list。(outside world->inside world)
print('User count:', len(info))#len(info)代表info這個dictionary有幾對key-value pair。
for item in info["comments"]:
    #print('count', item['count'])
    a = item["count"]
    n = int(a)
    lst.append(n)
print(sum(lst))
