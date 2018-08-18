# coding:utf-8
'''测试登录功能'''
import os
import sys
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.registerpage  import RegisterPageAction
from wap.src.common import comm

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

allscreenimg=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\tools\\all.png"
verifycodeimg=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\tools\\imgcode.png"

class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        #先准备注册数据
        cls.exist_username=cf.get("wapauto", "loginusername")
        cls.username = cf.get("wapauto", "register_username")
        cls.password = cf.get("wapauto", "register_password")



        # cls.driver = driver
        url = cf.get('wapauto', 'host')
        cls.registerpage = RegisterPageAction(driver, url)
        cls.registerpage.open()
        cls.registerpage.click_reigisterbtn()

        cls.registerpage.save_websitedomain(driver)



    def setUp(self):
        # print "in setup"


        if self.registerpage.is_on_registerpage():
            time.sleep(2)
            pass

        else:
            self.registerpage.enter_registerpage()

        pass

    @classmethod
    def tearDownClass(cls):
        # self.driver.quit()
        # driver.back()
        RegisterPageAction.backto_investpage(driver)
        pass


    def test_register_telexist(self):
        '''手机号已注册'''

        self.registerpage.input_registername(self.exist_username)

        time.sleep(1)
        self.registerpage.click_registerbtn()
        time.sleep(1)

        #弹窗处理及断言
        alert=self.registerpage.is_alert_exist()
        if alert[0]:
            #读取告警提示
            self.assertEqual(alert[1],"该用户已经存在！")
        else:
            self.assertTrue(alert[0],"没有告警弹窗")

    def test_register_success(self):
        '''注册正确'''

        self.registerpage.input_registername(self.username)

        #图片、短信验证码
        i=0
        imgverify_success=0
        for i in range(0,10):
            text=self.registerpage.get_imgverifycode(allscreenimg,verifycodeimg)
            if text !="":
                self.registerpage.input_imgverifycode(text)

                if self.registerpage.check_imgverifycode_right():
                    imgverify_success=1
                    break

        if i<10 and imgverify_success:
            #获取短信验证码
            msgcode=self.registerpage.get_msgverifycode(self.username)
            self.registerpage.input_msgverifycode(msgcode)

            pass
        else:
            print "无法校验图片验证码，请重试或手动输入"
            sys.exit(0)

        self.registerpage.input_registerpwd(self.password)
        self.registerpage.click_registerbtn()

        #注册成功断言
        time.sleep(2)
        result_text=self.registerpage.get_regiseterresult(driver)
        self.assertEqual(result_text[1],'恭喜您注册成功！')
        self.assertEqual(result_text[2],'为确保您的账户安全，请')
        self.assertEqual(result_text[3],'开通资金存管账户')


    def testCase3(self):

        self.assertEqual(2,2,"测试正确")

