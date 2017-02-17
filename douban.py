# -*- coding: utf-8 -*-
import urllib2
import re

def findMoive(values):
    url = 'https://www.douban.com/search?cat=1002&q='
    geturl = url+values
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile(r' <span class="rating_nums">(.*?)</span>')
    item = re.findall(pattern,content)
    if len(item) == 0 :
        return '没有找到这个电影'
    else:
        return '豆瓣评分:'+item[0]

