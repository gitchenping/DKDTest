# coding:utf-8
'''测试登录功能'''
import os
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.investpage import InvestPageAction

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=driver
        cls.investpage=InvestPageAction(driver)

        #投资前获取账户余额
        cls.beforeinvestamt = cls.investpage.get_accountamt()
        cls.afterinvestamt=cls.beforeinvestamt

        #进入项目列表页
        cls.investpage.click_wantinvestbtn()

        #先进入一个项目
        time.sleep(5)
        cls.investpage.select_investproject(20, 10000)
        # 投资前获取投资限额[起投金额，限额]
        cls.limitinvestamt = cls.investpage.get_limitinvestamt()
        cls.investpage.click_quickinvestbtn()


        # cls.tradingpassword=cf.get('wapauto','tradingpassword')

        pass

    def setUp(self):
        # if self.investpage.is_on_investpage():
        #     pass
        # # 如果当前页为我的账户页，需要先从充值入口进去
        # elif self.investpage.is_on_myaccountpage():
        #     self.investpage.click_wantinvestbtn()
        # else:
        #     self.investpage.enter_myaccountpage()
        pass

    def tearDown(self):
        self.beforeinvestamt=self.afterinvestamt

    @classmethod
    def tearDownClass(cls):

        # driver.quit()
        time.sleep(5)
        InvestPageAction.backto_investpage(driver)

        pass

    def test_invest_amtltmininvestamt(self):
        '''投资金额小于起投金额'''
        investamt=self.limitinvestamt[0]-1
        self.investpage.input_investamt(str(investamt))

        # 确认投资
        self.investpage.click_quickinvestbtn()

        time.sleep(1)
        alert =self.investpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "投资金额应大于起投金额")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

        # 进入投资输入金额页

        pass

    def test_invest_amtgtbalance(self):
        '''投资金额大于账户可用余额'''
        investamt = self.beforeinvestamt[1]+1
        self.investpage.input_investamt(str(investamt))

        # 确认投资
        self.investpage.click_quickinvestbtn()

        time.sleep(1)
        alert = self.investpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "账户可用余额不足")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

        pass



    def test_invest_amtgtmaxlimitamt(self):
        '''投资金额大于投资限额（投资上限、剩余可投）'''
        #投资上限>剩余可投
        if self.limitinvestamt[1]>self.limitinvestamt[2]:
            investamt=self.limitinvestamt[2]+1
            self.investpage.input_investamt(str(investamt))

            # 确认投资
            self.investpage.click_quickinvestbtn()

            time.sleep(1)
            alert =self.investpage.is_alert_exist()
            if alert[0]:
                # 读取告警提示
                self.assertEqual(alert[1], "投资金额应小于项目剩余金额")
            else:
                self.assertTrue(alert[0], "没有告警弹窗")
        else:
            investamt = self.limitinvestamt[1] + 1
            self.investpage.input_investamt(str(investamt))

            # 确认投资
            self.investpage.click_quickinvestbtn()

            time.sleep(1)
            alert = self.investpage.is_alert_exist()
            if alert[0]:
                # 读取告警提示
                self.assertEqual(alert[1], "投资总金额超出项目投资限额")
            else:
                self.assertTrue(alert[0], "没有告警弹窗")



        pass


    def test_invest_amteqmininvestamt(self):
        '''投资金额等于起投金额'''
        investamt=self.limitinvestamt[0]
        self.investpage.input_investamt(str(investamt))

        #确认投资
        self.investpage.click_quickinvestbtn()

        #投资后，剩余余额
        time.sleep(3)
        self.investpage.enter_myaccountpage()
        self.afterchargeamt = self.investpage.get_accountamt()

        #1、金额变化断言
        # print self.afterchargeamt
        self.assertEqual(self.afterchargeamt[0] , self.beforeinvestamt[0], "总资产正确")
        self.assertEqual(self.afterchargeamt[1] + float(investamt), self.beforeinvestamt[1], "可用余额正确")

        #2、投资项目列表显示断言



        pass
















