#coding=utf-8
import itchat
itchat.auto_login()
@itchat.msg_register(['Text'])
def text_reply(msg):
    itchat.send(u'Yes', msg['FromUserName'])
itchat.run()