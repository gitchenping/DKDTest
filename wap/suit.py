#coding=utf-8
import unittest

from cases.login import TestLogin
from cases.charge import TestCharge
from cases.withdraw import TestWithdraw
from cases.register import TestRegister
from cases.riskevaluate import TestRiskEvaluate
from cases.openaccount import TestOpenAccount
from cases.invest import TestInvest


#存量用户测试用例
def suite_stock():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()


    # suiteTest.addTest(TestLogin("test_login_wrongpassword"))
    suiteTest.addTest(TestLogin("test_login_success"))


    ################已注册未开户###########################
    #suiteTest.addTest(TestCharge("test_charge_withoutAccount"))
    # suiteTest.addTest(TestRiskEvaluate("test_riskevaluate_complete"))
    #
    # ########################充值######################
    # suiteTest.addTest(TestCharge("test_charge_null"))
    # suiteTest.addTest(TestCharge("test_charge_amtlthundred"))
    # suiteTest.addTest(TestCharge("test_charge_amteqhundred"))
    # suiteTest.addTest(TestCharge("test_charge_amtgthundred"))
    # suiteTest.addTest(TestCharge("test_charge_amtoverquota"))
    # suiteTest.addTest(TestCharge("test_charge_bankcharge"))

    # ####################提现#############################
    # suiteTest.addTest(TestWithdraw("test_withdraw_null"))
    # suiteTest.addTest(TestWithdraw("test_withdraw_over_todayavailabeamt"))
    # suiteTest.addTest(TestWithdraw("test_withdraw_over_availableamt"))
    # suiteTest.addTest(TestWithdraw("test_withdraw_over_realwithdrawamt"))
    # suiteTest.addTest(TestWithdraw("test_withdraw_within_availableamt"))

    suiteTest.addTest(TestWithdraw("test_commonwithdraw_fail"))

    ##########################投资项目###############################

    # suiteTest.addTest(TestInvest("test_invest_amtltmininvestamt"))
    # suiteTest.addTest(TestInvest("test_invest_amtgtbalance"))
    # suiteTest.addTest(TestInvest("test_invest_amteqmininvestamt"))

    # suiteTest.addTest(TestLogin("test_login_quit"))

    return suiteTest

#新注册用户用例
def suite_new():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()

    ###################注册#####################################
    # suiteTest.addTest(TestRegister("test_register_telexist"))
    suiteTest.addTest(TestRegister("test_register_success"))

    ############未开户用户充值、提现###########################
    # suiteTest.addTest(TestCharge("test_charge_withoutAccount"))
    suiteTest.addTest(TestWithdraw("test_withdraw_withoutAccount"))
    #
    #########################开户############################
    # suiteTest.addTest(TestOpenAccount("test_openaccount_success"))

    # ########################充值######################
    # suiteTest.addTest(TestCharge("test_charge_null"))
    # suiteTest.addTest(TestCharge("test_charge_amtlthundred"))
    # suiteTest.addTest(TestCharge("test_charge_amteqhundred"))
    # suiteTest.addTest(TestCharge("test_charge_amtgthundred"))
    # suiteTest.addTest(TestCharge("test_charge_amtoverquota"))
    # suiteTest.addTest(TestCharge("test_charge_bankcharge"))

    #######################风险偏好#############################
    # suiteTest.addTest(TestRiskEvaluate("test_riskevaluate_left"))
    #
    # suiteTest.addTest(TestRiskEvaluate("test_riskevaluate_complete"))

    ##########################投资项目###############################

    # suiteTest.addTest(TestInvest("test_invest_amtltmininvestamt"))
    # suiteTest.addTest(TestInvest("test_invest_amtgtbalance"))
    # suiteTest.addTest(TestInvest("test_invest_amteqmininvestamt"))

    return suiteTest

