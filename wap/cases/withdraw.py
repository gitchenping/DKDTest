# coding:utf-8
'''测试登录功能'''
import os
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.withdrawpage  import WithdrawPageAction

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

class TestWithdraw(unittest.TestCase):

    #实例不能放到这里
    # withdrawpage = WithdrawPageAction(driver)
    # beforewithdrawamt = withdrawpage.get_accountamt()

    @classmethod
    def setUpClass(cls):
        # cls.driver=driver
        cls.withdrawpage=WithdrawPageAction(driver)

        # 提现前总金额及可用余额
        cls.beforewithdrawamt = cls.withdrawpage.get_accountamt()
        cls.afterwithdrawamt = cls.beforewithdrawamt

        #进入提现页面
        cls.withdrawpage.click_withdrawbtn()

        # 充值金额、提现金额及交易密码
        # 提现金额
        withdrawlist = cf.get('wapauto', 'withdrawamt')
        cls.withdrawlist = withdrawlist.split(',')

        cls.tradingpassword = cf.get('wapauto', 'tradingpassword')
        pass

    def setUp(self):
        if self.withdrawpage.is_on_withdrawpage():
            pass
        else:
            #进入我的账户\提现页
            self.withdrawpage.enter_myaccountpage()
            self.beforewithdrawamt = self.withdrawpage.get_accountamt()
            self.withdrawpage.click_withdrawbtn()

        pass

    @classmethod
    def tearDownClass(cls):
        # cls.aa=11
        # driver.quit()
        WithdrawPageAction.backto_investpage(driver)
        time.sleep(5)
        pass

    def tearDown(self):
        #将提现后金额重新赋值
        # self.beforewithdrawamt[0] = self.afterchargeamt[0]
        # self.beforewithdrawamt[1] = self.afterchargeamt[1]
        self.beforewithdrawamt = self.afterwithdrawamt
        pass


    def test_withdraw_null(self):
        '''提现金额为空'''

        #测试输入金额
        self.withdrawpage.input_withdrawamt(self.withdrawlist[0])
        self.withdrawpage.click_withdrawtoaccountbtn()

        # 弹窗处理及断言
        alert = self.withdrawpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "金额不能为空")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

    def test_withdraw_over_todayavailabeamt(self):
        '''可提现金额不足(先代扣充值)'''
        # 提现金额=可提取金额+1（前提条件，先进行了代扣充值）

        amount=self.withdrawpage.get_todayavailableamt()+1
        amount=str(amount)
        #测试输入
        self.withdrawpage.input_withdrawamt(amount)
        self.withdrawpage.click_withdrawtoaccountbtn()

        # 弹窗处理及断言
        alert = self.withdrawpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "可提现金额不足，由于您当日进行了代扣充值，代扣充值金额下一工作日可提现")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")



    def test_withdraw_over_availableamt(self):
        '''超过可提现金额'''

        # 测试输入金额
        self.withdrawpage.input_withdrawamt(self.withdrawlist[1])
        self.withdrawpage.click_withdrawtoaccountbtn()

        # 弹窗处理及断言
        alert = self.withdrawpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "可提现金额不足")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

    def test_withdraw_over_realwithdrawamt(self):
        '''实时提现大于50000元'''
        # 测试输入金额
        self.withdrawpage.input_withdrawamt(self.withdrawlist[2])
        self.withdrawpage.click_withdrawtoaccountbtn()

        # 弹窗处理及断言
        alert = self.withdrawpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "提现金额不能大于50000元")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

    def test_withdraw_within_availableamt(self):
        '''实时提现金额小于可提现金额'''
        # 测试输入金额
        amount=self.withdrawlist[3]
        self.withdrawpage.input_withdrawamt(amount)
        self.withdrawpage.click_withdrawtoaccountbtn()

        # 提现成功断言
        #1.结果页


        #2.提现前后，金额关系断言
        time.sleep(3)
        self.withdrawpage.enter_myaccountpage()
        # afterchargeamt = self.withdrawpage.get_accountamt()

        self.afterwithdrawamt = self.withdrawpage.get_accountamt()

        self.assertEqual(self.afterwithdrawamt[0] + float(amount), self.beforewithdrawamt[0], "总资产正确")
        self.assertEqual(self.afterwithdrawamt[1] + float(amount), self.beforewithdrawamt[1], "可用余额正确")

        # 更新金额
        # self.beforewithdrawamt[0] = afterchargeamt[0]
        # self.beforewithdrawamt[1] = afterchargeamt[1]


        #3.交易记录断言


    def test_commonwithdraw_fail(self):
        '''大额提现提现金额小于50000'''
        amount=49999
        self.withdrawpage.enter_commonwithdrawpage()

        self.withdrawpage.input_withdrawamt(amount,False)
        self.withdrawpage.click_withdrawtoaccountbtn(False)

        #提现结果断言
        # 弹窗处理及断言
        alert = self.withdrawpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "提现金额不能小于等于50000元")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")


        pass


    def test_commonwithdraw(self):
        '''大额提现正常50001（账户可提现金额大于50001）'''
        amount = 50001
        # self.withdrawpage.enter_commonwithdrawpage()

        self.withdrawpage.input_withdrawamt(amount, False)
        self.withdrawpage.click_withdrawtoaccountbtn(False)



        pass




    def test_withdraw_withoutAccount(self):
        '''未开户提现'''

        text = self.withdrawpage.noaccount_alert()

        self.assertEqual(text, "您尚未开通银行资金存管账户")






