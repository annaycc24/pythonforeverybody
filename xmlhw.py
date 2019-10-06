#某人依據XML Schema寫出了XML，依照我們看到的XML的格式去寫程式，以便找出我們要的tag，並取出資料。
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
print(html)
lst = list()
x = ET.fromstring(html) #將html轉成數狀圖，有點像json的loads的功能。(outside world->inside world)
y = x.findall("comments/comment")#和.find的區別在於這個是要找更細節的”子tag”
for item in y:
    c = item.find("count").text
    #print(c)
    C = int(c)
    lst.append(C)
    #list 沒有回傳值 所以單純append數字會print不出來
print(sum(lst))
