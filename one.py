# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
def getcot(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()  # 得到网页内容\
    return content

def getImage(url):
    local = 'one.jpg'
    urllib.urlretrieve(url, local)

def getOneText():
    content=getcot('http://wufazhuce.com/')
    pattern = re.compile(r'<a href="(.*?)"><img class="fp-one-imagen" src="(.*?)" alt="" /></a>')
    item = re.findall(pattern, content)
    url=item[0][0]
    getImage(item[0][1])
    content2=getcot(url)
    str(content2).decode('utf-8')
    s=str(content2)
    x=s.find('default_text="')
    x=x+14
    y=s.find('"',x)
    return s[x:y]


