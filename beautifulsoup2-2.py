#透過beautifulsoup這個方法去網頁(一般網頁，較雜亂，不同於XML Schema和API有格式可言。)找我們要的tag，不同於json和XML，他們比較像是一種表示的格式，而beautifulsoup是一種爬蟲方法
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def URL(url,c,p):
    #count = 0
    count1 = 0#while迴圈的計數器要寫在while迴圈外，不然迴圈不會停，因為計數器在迴圈中的話會一直歸零。
    c = int(c) #注意input的"3"只是字串，python不會自動轉成數字去理解，因此這邊要先轉成數字。
    p = int(p)
    while count1<c: #或是用while True也可以
        #url = n
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")#和json的loads＆XML的fromstring類似功能。(outside world->inside world)
        tags = soup('a')
        count = 0 #這個計數器是給for迴圈的 要寫在裡面，不然for迴圈的計數器不會歸零，會一直加上去。
        for tag in tags:
            n = tag.get("href", None)
            count = count+1
            if count == p:
                break
        url = n
        #print(n)
    #    return(n)#注意縮排，這一條code是結果，因此是在迴圈外
        count1 = count1+1
        #如果用while True，這邊需要加上if count1 == c: break，不然迴圈不會停
    return(n)

url = input("ENTER URL: ")
c = input("ENTER COUNT: ")
p = input("ENTER POSITION: ")
print(URL(url,c,p))
