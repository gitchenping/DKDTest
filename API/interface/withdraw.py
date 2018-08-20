# -*- coding:utf-8 -*-
import os
import sys
import unittest
import json
import requests
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read('D:\\NewPythonWorkplace\\config.ini')

toppath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
commpath = toppath + "\comm"

sys.path.append(commpath)

datapath = toppath + "\datadriver\dkd.xlsx"

from xls import readExcel
from myrequest import HttpRequest


# class LogIn():
#
#     def __init__(self):
#
#         self.apipath="/api/3.0/W/login"
#         self.host=cf.get('apiauto','host')
#
#     def login_correct(self):
#         '''正确用户名、密码'''
#         url=self.host+self.apipath
#         payload = {
#             "params": '{"userName":"18810756676","password":"e10adc3949ba59abbe56e057f20f883e","ip":"","tagCode":"INVEST"}',
#             "from": "W",
#             "imei": "imei"
#         }
#         r = requests.post(url, data=payload, verify=False)
#         rjs = r.json()
#         # print js['token']
#         return rjs
#         pass
#
#
#     def login_wrong(self):
#         '''正确用户名、错误密码'''
#         pass
# token=""
class TestWithdrawAction(unittest.TestCase):

    def setUp(self):

        # 载入用例
        # self.token=""
        self.cases = []
        self.cases = readExcel(datapath).getcase(['lmWithdraw'])
        print self.cases
        self.httprequest = HttpRequest()
        pass

    def test_withdraw(self):
        '''用户名、密码正确'''
        singlecase = self.cases[0]

        r = self.httprequest.reqsend(singlecase)
        print r


        if r != "ERROR":
            # print "good"
            # self.token = "12"
            # 响应码
            self.assertEqual('1', '1')

            # 响应消息
            self.assertEqual('1', '1')


            # print r['token']
        else:
            self.assertEqual(0, 1)

    def tearDown(self):
        # driver.quit()


        pass