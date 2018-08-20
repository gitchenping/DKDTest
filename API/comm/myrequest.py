# -*- coding:utf-8 -*-
import requests
import os
toppath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
tokenpath=toppath+"\\token.md"

class HttpRequest(object):
    method =""
    url = ""
    payload = ""

    def __init__(self):

        pass

    def reqsend(self,singlecase):

        method = singlecase[5]
        url = singlecase[3] + singlecase[4]
        #转为字典
        payload = eval(singlecase[6])

        #在payload中填充token
        params=eval(payload['params'])
        if params.has_key('token') and params['token']=="":
            #读文件
            with open(tokenpath, 'r') as f:
               token =f.read()
               params['token']=token
            #转换为字符串插入
            payload['params'] = str(params)

        # print payload
        if method=='post':

            r=requests.post(url, data=payload, verify=False)
        elif method=='get':

            r=requests.get(url, data=payload, verify=False)
        else:
            pass
        # print str(r)

        if  str(r).find("404")!=-1:
            print "连接失败，请检查服务器"
            return "ERROR"
        elif str(r).find("400")!=-1:
            print "请求失败，请检查请求是否合法"
            return "ERROR"
        else:
            return r.json()
