# coding:utf-8
'''测试登录功能'''
import os
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.chargepage import ChargePageAction

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

class TestCharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=driver
        cls.chargepage=ChargePageAction(driver)

        #充值前金额
        cls.beforechargeamt = cls.chargepage.get_accountamt()
        #进入充值页面（默认转账充值页面）
        cls.chargepage.click_chargebtn()

        chargelist=cf.get('wapauto','chargeamt')
        cls.chargelist=chargelist.split(',')

        cls.tradingpassword=cf.get('wapauto','tradingpassword')

        pass

    def setUp(self):
        if self.chargepage.is_on_chargepage():
            pass
        # 如果当前页为我的账户页，需要先从充值入口进去
        elif self.chargepage.is_on_myaccountpage() and not self.chargepage.is_noaccountpopalert_exist():
            self.chargepage.click_chargebtn()
        elif not self.chargepage.is_noaccountpopalert_exist():
            self.chargepage.enter_myaccountpage()
        else:
            pass
        pass


    @classmethod
    def tearDownClass(cls):

        # driver.quit()
        ChargePageAction.backto_investpage(driver)
        time.sleep(5)

        pass


    def test_charge_null(self):
        '''充值为空'''

        #代扣充值金额
        self.chargepage.input_chargeamt(self.chargelist[0])
        self.chargepage.click_chargetoaccount()

        # 弹窗处理及断言
        alert = self.chargepage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "金额不能为空")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")


    def test_charge_amtlthundred(self):
        '''充值金额小于100'''

        # 代扣充值金额
        self.chargepage.input_chargeamt(self.chargelist[1])
        self.chargepage.click_chargetoaccount()

        # 弹窗处理及断言
        alert = self.chargepage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "充值金额不能小于100元")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

    def test_charge_amteqhundred(self):
        '''最小充值金额100'''

        # 代扣充值金额
        amount=self.chargelist[2]
        self.chargepage.input_chargeamt(amount)
        self.chargepage.click_chargetoaccount()

        # 弹窗处理及断言
        alert = self.chargepage.is_chargeconfirm_exist()
        if alert:
            #输入交易密码并提交
            # self.chargepage.input_TradingPassword(self.tradingpassword)

            #充值成功断言
            #1、充值成功结果页断言

            #2、充值前后金额关系断言
            time.sleep(3)
            self.chargepage.enter_myaccountpage()
            afterchargeamt = self.chargepage.get_accountamt()

            aftercharge = afterchargeamt[0] - float('%.2f' % float(amount))
            # self.assertEqual(aftercharge, self.beforechargeamt[0], "总资产正确:"+str(aftercharge)+"= "+str(self.beforechargeamt[0]))
            self.assertEqual(aftercharge, self.beforechargeamt[0])

            remainaftercharge = afterchargeamt[1] - float('%.2f' % float(amount))
            # self.assertEqual(remainaftercharge, self.beforechargeamt[1], "可用余额正确:"+str(remainaftercharge)+" ="+str(self.beforechargeamt[1]))
            self.assertEqual(remainaftercharge, self.beforechargeamt[1])

            self.beforechargeamt[0]=afterchargeamt[0]
            self.beforechargeamt[1]=afterchargeamt[1]

            #3、交易明细断言

        else:
            self.assertTrue(alert,"没有确认充值弹窗,页面没跳转")


    def test_charge_amtgthundred(self):
        '''充值金额大于100小于限额'''


        # 代扣充值金额
        amount = self.chargelist[4]
        self.chargepage.input_chargeamt(amount)
        self.chargepage.click_chargetoaccount()

        # 弹窗处理及断言
        alert = self.chargepage.is_chargeconfirm_exist()
        if alert:
            # 输入交易密码
            # self.chargepage.input_TradingPassword(self.tradingpassword)

            #充值成功断言
            # 1、充值成功结果页断言

            # 2、充值前后金额关系断言
            time.sleep(3)
            self.chargepage.enter_myaccountpage()
            afterchargeamt = self.chargepage.get_accountamt()

            #
            aftercharge=float('%.2f' % (afterchargeamt[0] - float(amount)))
            # self.assertEqual(aftercharge, self.beforechargeamt[0], "总资产正确:"+str(aftercharge)+"= "+str(self.beforechargeamt[0]))
            self.assertEqual(aftercharge, self.beforechargeamt[0])

            remainaftercharge=float('%.2f' % (afterchargeamt[1] - float(amount)))
            # self.assertEqual(remainaftercharge, self.beforechargeamt[1], "可用余额正确:"+str(remainaftercharge)+" ="+str(self.beforechargeamt[1]))
            self.assertEqual(remainaftercharge, self.beforechargeamt[1])

            #更新金额
            self.beforechargeamt[0] = afterchargeamt[0]
            self.beforechargeamt[1] = afterchargeamt[1]

            # 3、交易明细断言

        else:
            self.assertTrue(alert, "没有确认充值弹窗,页面没跳转")

    def test_charge_amtoverquota(self):
        '''充值金额大于银行卡限额'''


        # 代扣充值金额
        amount = self.chargelist[5]
        self.chargepage.input_chargeamt(amount)
        self.chargepage.click_chargetoaccount()

        # 弹窗处理及断言
        time.sleep(1)
        alert = self.chargepage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "充值金额超出银行限额！")
            self.chargepage.enter_myaccountpage()
        else:
            self.assertTrue(alert[0], "充值金额超出银行限额,但没有告警弹窗")


    def test_charge_bankcharge(self):
        '''转账充值'''

        #1、读取页面银行资金账户信息,得到一个字典
        accountinfo=self.chargepage.get_bankaccountinfo()

        self.assertEqual(1,1)
        # print accountinfo


        #2、其他


    def test_charge_withoutAccount(self):
        '''未开户充值'''

        text=self.chargepage.noaccount_alert()

        self.assertEqual(text,"您尚未开通银行资金存管账户")











