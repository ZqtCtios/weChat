#coding=utf-8
import urllib2
import re
def findNews():
    url = 'http://news.sina.com.cn/hotnews/'
    print url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read() #得到网页内容\
    pattern = re.compile(r'<tr><td>\d+</td><td class=\'ConsTi\'><a href=\'(.*?)\' target=\'_blank\' >(.*?)</a>')
    item = re.findall(pattern,content)
    s=''
    news=[]
    sum=0
    for i in item:
        s=s+i[0]+u' '+i[1]+'\n'
        sum=sum+1
        if sum==10:
            news.append(s)
            s=''
            sum=0
    return news