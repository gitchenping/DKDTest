# coding=utf-8

import os
import sys
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.openaccountpage import OpenAccountAction
from wap.src.common.comm import PersonInfo,get_IDIMG

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

wappath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
toolpath=wappath+"\\tools\\"

headimgpath=toolpath+"portraiture.png"
emblemimgpath=toolpath+"nationalemblem.png"


def create_mockaccountinfo():

    #开户四要素
    identify = cf.get('wapauto', 'open_account_ID')
    bankcardid = cf.get('wapauto', 'open_account_BANKNo')

    person = PersonInfo()
    realname = person.get_Newname()

    if not identify and not bankcardid:

        identify = person.get_NEWID()
        bankcardid = person.get_BANKCARDID()
    elif not identify:
        identify = person.get_NEWID()
    elif not bankcardid:
        bankcardid = person.get_BANKCARDID()
    else:
        pass

    return [realname,identify,bankcardid]

class TestOpenAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver=driver
        cls.openaccountpage=OpenAccountAction(driver)

        #进入开户页
        cls.openaccountpage.click_accountbtn()

        #开户前先构造身份证
        accountinfo=create_mockaccountinfo()

        cls.realname=accountinfo[0]
        cls.identify=accountinfo[1]
        cls.bankid=accountinfo[2]

        #生成身份证图片
        get_IDIMG(cls.realname,cls.identify)

        pass

    @classmethod
    def tearDownClass(cls):
        OpenAccountAction.goback_mainpage(driver)
        time.sleep(5)

    def setUp(self):
        # if self.chargepage.is_on_chargepage():
        #     pass
        # # 如果当前页为我的账户页，需要先从充值入口进去
        # elif self.chargepage.is_on_myaccountpage():
        #     self.chargepage.click_chargebtn()
        # else:
        #     self.chargepage.enter_myaccountpage()
        pass



    def test_openaccount_opened(self):
        '''已开户，重复开户'''

    def test_openaccount_success(self):
        self.openaccountpage.input_realname(self.realname)
        self.openaccountpage.input_id(self.identify)
        self.openaccountpage.input_bankid(self.bankid)
        self.openaccountpage.select_bank()
        self.openaccountpage.input_mobile("18811345809")

        #提交进入身份证上传页面
        self.openaccountpage.click_nextstepbtn()

        self.openaccountpage.uploadimg(headimgpath,emblemimgpath)
        #提交开户
        self.openaccountpage.submit_openaccout()

        #懒猫页面
        # 填写交易密码
        self.openaccountpage.input_smsverifycode()
        self.openaccountpage.smsalert_click()
        self.openaccountpage.input_smspassword()
        # 同意协议
        self.openaccountpage.agree_protocol()

        # #assert
        result = self.openaccountpage.openaccount_result()
        self.assertEqual(result, True)






