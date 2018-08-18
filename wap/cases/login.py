# coding:utf-8
'''测试登录功能'''
import os
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.loginpage import LoginPageAction

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = driver
        url = cf.get('wapauto', 'host')
        cls.loginpage = LoginPageAction(driver, url)
        cls.loginpage.open()

        cls.loginpage.save_websitedomain(driver)

    def setUp(self):
        # print "in setup"
        self.username = cf.get("wapauto", "loginusername")
        self.password = cf.get("wapauto", "loginpassword")

        pass

    def tearDown(self):
        # self.driver.quit()
        time.sleep(1)
        pass


    def test_login_wrongpassword(self):
        '''用户名正确、密码错误'''

        self.loginpage.input_username(self.username)
        self.loginpage.input_password("000000")
        time.sleep(1)
        self.loginpage.click_submitbtn()
        time.sleep(1)

        #弹窗处理及断言
        alert=self.loginpage.is_alert_exist()
        if alert[0]:
            #读取告警提示
            self.assertEqual(alert[1],"用户名或密码错误")
        else:
            self.assertTrue(alert[0],"没有告警弹窗")

    def test_login_success(self):
        '''用户名、密码正确'''
        # login= LoginAction()

        self.loginpage.input_username(self.username)
        self.loginpage.input_password(self.password)

        time.sleep(1)
        self.loginpage.click_submitbtn()
        time.sleep(3)

        # self.loginpage.is_myaccoutlink_exist()
        self.assertTrue(self.loginpage.is_myaccoutlink_exist(),"登录成功")


    def test_login_quit(self):
        '''退出'''

        driver.quit()

