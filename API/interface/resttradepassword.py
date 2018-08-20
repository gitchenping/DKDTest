# -*- coding:utf-8 -*-

import unittest
import json
import requests
import ConfigParser

cf=ConfigParser.ConfigParser()
cf.read('D:\\NewPythonWorkplace\\config.ini')

class TestResetPasswordAction(unittest.TestCase):

    def setUp(self):
        self.apipath = "/api/3.0/W/lmService/resetPassword"
        self.host = cf.get('apiauto', 'host')
        pass

    def test_resetpwd(self):
        '''token正确'''

        url = self.host + self.apipath
        payload = {
            "params": '{"token":"c854ae960729459eac7d56499872c228"}',
            "from": "W",
            "imei": "imei"
        }
        r = requests.post(url, data=payload, verify=False)
        rjs = r.json()
        rescode = rjs['resCode']
        resmsg = rjs['resMsg']
        # print rjs
        # 响应码
        self.assertEqual(rescode, '0000')
        # 响应消息
        self.assertEqual(resmsg, '成功')


    def test_login_fail(self):
        '''token错误'''

        url = self.host + self.apipath
        payload = {
            "params": '{"token":"c854ae960729459eac7d56499872c229"}',
            "from": "W",
            "imei": "imei"
        }
        r = requests.post(url, data=payload, verify=False)
        rjs = r.json()
        rescode = rjs['resCode']
        resmsg = rjs['resMsg']
        print rjs
        # 响应码断言
        self.assertEqual(rescode, 'E0000002')
        # 响应消息
        self.assertEqual(resmsg, 'token信息已失效或非法')

        # self.assertEqual("1","1","密码不正确")