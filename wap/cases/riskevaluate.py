# coding:utf-8
'''测试登录功能'''
import os
import time
import unittest
import ConfigParser

from wap.config.Driver import driver
from wap.src.pages.riskevaluatepage import RiskEvaluateAction

config_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)


class TestRiskEvaluate(unittest.TestCase):

    #实例不能放到这里
    # withdrawpage = WithdrawPageAction(driver)
    # beforewithdrawamt = withdrawpage.get_accountamt()

    @classmethod
    def setUpClass(cls):
        # cls.driver=driver
        cls.riskpage=RiskEvaluateAction(driver)

        cls.riskpage.enter_questionare()

        cls.answer = cf.get('wapauto', 'questionanswer_list')


        pass

    def setUp(self):


        pass

    @classmethod
    def tearDownClass(cls):
        # cls.aa=11
        # driver.quit()
        RiskEvaluateAction.backto_investpage(driver)
        pass

    def tearDown(self):
        #将提现后金额重新赋值
        # self.beforewithdrawamt[0] = self.afterchargeamt[0]
        # self.beforewithdrawamt[1] = self.afterchargeamt[1]
        pass


    def test_riskevaluate_left(self):
        '''没有完成答题'''
        self.riskpage.click_questionnaire_submitbtn()

        # 弹窗处理及断言
        alert = self.riskpage.is_alert_exist()
        if alert[0]:
            # 读取告警提示
            self.assertEqual(alert[1], "问卷还没答完哦～")
        else:
            self.assertTrue(alert[0], "没有告警弹窗")

        pass

    def test_riskevaluate_complete(self):
        '''全部答题'''
        if self.answer=="":
            self.riskpage.answer_question()
        else:
            answerlist = self.answer.split(',')
            self.riskpage.answer_question(answerlist)
        self.riskpage.click_questionnaire_submitbtn()

        #评估结果断言
        risktype=self.riskpage.get_userrisktype()
        self.assertEqual(risktype,"稳健型")

        pass










