# coding=utf-8

import unittest
import time
import os
import ConfigParser

from APP.src.pages.capaccountpage import CapAccountPage
from APP.config.By import PORTAL_LOC,MYACCOUNT_LOC,LMOpen_LOC


config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

wappath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
toolpath=wappath+"\\tools\\"

headimgpath=toolpath+"portraiture.png"
emblemimgpath=toolpath+"nationalemblem.png"


# class TestOpenAccount(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         #此函数中所有的函数调用都要通过实例调用的方法来使用，否则报错：AttributeError: '_TestResult' object has no attribute 'outputBuffer'
#
#         cls.openaccount=CapAccountPage(PORTAL_LOC['Myaccount'],MYACCOUNT_LOC['CapAccount'])
#
#         #开户信息确认
#         # 开户四要素
#
#         name =cf.get('appauto', 'open_account_realname').decode('utf-8')
#         identify = cf.get('appauto', 'open_account_id')
#         bankcardid = cf.get('appauto', 'open_account_bankcard')
#         tel =cf.get('appauto', 'open_account_tel')
#
#         cls.accountinfo=cls.openaccount.init_accountinfo(realname=name,id=identify,bankcard=bankcardid,tel=tel)
#         cls.openaccount.push_idimg(headimgpath)
#
#         pass
#
#     def tearDown(self):
#         pass
#
#
#     def setUp(self):
#         # print "in setup"
#
#         pass
#
#
#
#     def test_openaccount_success(self):
#         '''新用户开户成功'''
#         #1、开户信息填写
#
#         self.openaccount.fill_capaccount_info(self.accountinfo[0],self.accountinfo[1],self.accountinfo[2],self.accountinfo[3])
#
#         #2、上传身份证照片
#
#         self.openaccount.uploadidshot()
#
#         #3、交易密码设置
#         time.sleep(5)
#         self.openaccount.fill_lminfo("999999")
#
#         #4、提交开户并做断言
#
#         #检查姓名和身份证号
#         result=self.openaccount.check_accountinfo(self.accountinfo[0],self.accountinfo[1])
#
#         self.assertTrue(result,'开户成功，账户信息正确')
#
#         pass






openaccount=CapAccountPage(PORTAL_LOC['Myaccount'],MYACCOUNT_LOC['CapAccount'])

name =cf.get('appauto', 'open_account_realname').decode('utf-8')
identify = cf.get('appauto', 'open_account_id')
bankcardid = cf.get('appauto', 'open_account_bankcard')
tel =cf.get('appauto', 'open_account_tel')

accountinfo=openaccount.init_accountinfo(realname=name,id=identify,bankcard=bankcardid,tel=tel)
openaccount.push_idimg(headimgpath)

openaccount.fill_capaccount_info(accountinfo[0],accountinfo[1],accountinfo[2],accountinfo[3])
openaccount.uploadidshot()
openaccount.fill_lminfo("999999")

# from appium.webdriver.common.mobileby import MobileBy
# nav=(MobileBy.CLASS_NAME,'android.widget.TextView')
# ele=openaccount.findElements(nav)
# print ele
# print ele[1].text