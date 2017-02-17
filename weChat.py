#coding=utf-8
import itchat
import one
import urllib
import turing
import douban

def getImage(url):
    local = 'one.jpg'
    urllib.urlretrieve(url, local)

def findType(text):
    type=[u'r+',u'one',u'One',u'db+',u'help']
    for i in range(len(type)):
        if text.find(type[i]) == 0:
            return i
    return -1

oneText=one.getOneText()
itchat.auto_login()
@itchat.msg_register(['Text']) #针对文字信息回复
def text_reply(msg):
    ss=msg['Text']
    print ss
    typeNumber=findType(ss)
    if typeNumber == 1 or typeNumber == 2:   #One功能
        print oneText
        itchat.send(oneText.decode('utf-8'),msg['FromUserName'])
        itchat.send('@%s@%s' % ('img','one.jpg'), msg['FromUserName'])
    elif typeNumber == 0:                    #机器人回复
        ss = ss[2:len(ss)]
        ss = ss.encode('utf-8')
        text=turing.turing(msg['FromUserName'][1:20].encode('utf-8'),ss)
        print text
        itchat.send(text, msg['FromUserName'])
    elif typeNumber == 3:                   #豆瓣评分
        ss=ss[3:len(ss)]
        ss=ss.encode('utf-8')
        text=douban.findMoive(ss).decode('utf-8')
        itchat.send(text, msg['FromUserName'])
    elif typeNumber == 4:                   #帮助
        text=u'使用教程如下\n' \
             u'\"r+文字\" 如 r+你好 向机器人问话\n' \
             u'\"db+电影\" 如 db+大话西游 查询豆瓣评分\n' \
             u'\"help\" 打开帮助\n' \
             u'\"one(One)\" 获取one'
        itchat.send(text, msg['FromUserName'])
itchat.run()
