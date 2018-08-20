# coding=utf-8

import unittest
import time
from APP.src.common.uihelper import Driver,unlockgesture
from APP.src.common.basepage import BasePage
from APP.config.By import LOGIN_LOC




class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.login=BasePage()
        pass


    def setUp(self):
        # print "in setup"


        pass

    def tearDown(self):
        # self.driver.quit()

        pass


    def test_login_wrongpassword(self):
        '''用户名正确、密码错误'''



        #弹窗处理及断言


    def test_login_success(self):
        '''用户名、密码正确'''

        loginelement=self.login.comfindElement(LOGIN_LOC["LoginSub"])
        loginelement.click()


        # print tuple(eval(LOGIN_LOC['cachelayout']))
        # if self.login.is_element_exist(tuple(eval(LOGIN_LOC['cachelayout']))):
        #     self.login.findElement(tuple(eval(LOGIN_LOC['cachelayout']))).click()

        #手机号、密码

        self.login.send_keys(LOGIN_LOC['LoginPwd'], '123456')
        self.login.send_keys(LOGIN_LOC['Tel'], '18811345809')
        #
        self.login.comfindElement(LOGIN_LOC["LoginBtn"]).click()

        ementsize=self.login.getElementsize(LOGIN_LOC['GesturPwd'])

        gesture_dotlist = [(1,2),(2, 1), (2, 2), (2, 3), (3, 2)]
        unlockgesture(self.login.driver,ementsize,*gesture_dotlist)
        time.sleep(3)
        unlockgesture(self.login.driver, ementsize, *gesture_dotlist)

        #
        close = 'com.pitaya.daokoudai:id/iv_close'
        # pos=(MobileBy.ID,close)
        if self.login.is_element_exist(close):
            self.login.comfindElement(close).click()
        else:
            print "no bad"






