# -*- coding:utf-8 -*-

#test framework
import unittest
import HTMLTestRunnerCN
import time
import sys
# import HTMLTestRunner
import HTMLTestRunnerCN
import ConfigParser
from  Driver import driver
# from login import LoginAction
from loginpage import LoginPageAction
from register import RegisterPageAction
from openaccountpage import OpenAccountAction
from riskevaluatepage import RiskEvaluateAction

from invest import InvestPageAction
from charge import ChargeAction
from withdraw import WithdrawAction

from myaccount import MyaccountAction
from mouse import mouse_click


cf=ConfigParser.ConfigParser()
cf.read('D:\\NewPythonWorkplace\\config.ini')
#
#测试用例
class TestLogin(unittest.TestCase):

    def setUp(self):
        # driver.get(webcfg.url)
        # print "in setup" + str(type(time))
        self.driver=driver
        self.url=cf.get('webauto', 'host')
        pass

    def tearDown(self):
        # self.driver.quit()
        pass

    def test_login(self):
        # login= LoginAction()
        # name=login.login()       #return login_name

        loginpage = LoginPageAction(self.driver, self.url)

        loginpage.open()
        loginpage.click_account()

        # time.sleep(3)
        username = cf.get("webauto", "loginusername")
        password = cf.get("webauto", "loginpassword")
        loginpage.input_username(username)
        loginpage.input_password(password)
        # loginpage.click_submit()
        time.sleep(5)
        mouse_click(900, 570)
        time.sleep(15)


        # name=loginpage.show_userid()
        # self.assertEqual(name,webcfg.name_show,"successful")

    def testCase2(self):
        self.assertEqual(2+1,3,"testError")

    def testCase3(self):
        self.assertEqual(2,2,"测试正确")

class TestRegister(unittest.TestCase):
    def setUp(self):
        # driver.get(webcfg.url)
        # print "in setup" + str(type(time))
        self.driver=driver
        self.url = cf.get('webauto', 'host')
        pass

    def tearDown(self):
        # self.driver.quit()
        pass

    def test_register(self):
        # login= LoginAction()
        # name=login.login()       #return login_name

        registerpage = RegisterPageAction(self.driver, self.url)

        registerpage.open()
        #注册页面
        registerpage.click_account()

        #输入手机号、密码
        registerpage.input_username()
        registerpage.input_password()

        #图片、短信验证码识别
        registerpage.screen_img_shot()
        #
        registerpage.click_submit()

        time.sleep(5)

class TestOpenAccount(unittest.TestCase):
    def setUp(self):

        self.driver=driver
        self.url=cf.get('webauto','host')
        pass

    def tearDown(self):
        # self.driver.quit()
        pass

    def test_openaccount(self):

        loginpage = LoginPageAction(self.driver, self.url)
        newaccount_username = cf.get("webauto", "open_account_name")
        newaccount_password = cf.get("webauto", "open_account_password")
        loginpage.login(newaccount_username,newaccount_password)

        #开户页面打开
        openaccountpage=OpenAccountAction(self.driver)
        openaccountpage.openaccount_click()
        time.sleep(1)

        #构造开户信息
        openaccountpage.getaccountinfo()

        # #填写字段
        openaccountpage.accountinfo_submit()

        #上传身份证
        openaccountpage.uploadimg()

        #提交开户
        openaccountpage.submit_openaccout()
        time.sleep(5)
        # #填写交易密码
        openaccountpage.input_smsverifycode()
        openaccountpage.input_smspassword()
        # #同意协议
        openaccountpage.agree_protocol()
        # #assert
        # result=openaccountpage.openaccount_result()
        # self.assertEqual(result,True)


class TestRiskevaluate(unittest.TestCase):
    def setUp(self):

        self.driver=driver
        self.url=cf.get('webauto','host')
        pass

    def tearDown(self):
        # self.driver.quit()
        pass

    def test_riskevaluate(self):

        loginpage = LoginPageAction(self.driver, self.url)
        newaccount_username = cf.get("webauto", "open_account_name")
        newaccount_password = cf.get("webauto", "open_account_password")
        loginpage.login(newaccount_username,newaccount_password)

        #评估页面打开
        riskevaluatepage=RiskEvaluateAction(self.driver)
        riskevaluatepage.enter_riskevaluate()
        riskevaluatepage.answer_question()


class TestCharge(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.url = cf.get('webauto', 'host')
        loginpage = LoginPageAction(self.driver, self.url)
        username = cf.get("webauto", "loginusername")
        password = cf.get("webauto", "loginpassword")
        loginpage.login(username, password)

        pass

    def tearDown(self):
        # driver.quit()
        pass

    def test_charge(self):
        charge=ChargeAction(self.driver,self.url)
        available_amount=charge.charge()

        #read availableAmt
        self.assertEqual(available_amount[0]+int(cf.get('webauto','chargeamount')), available_amount[1], "testSuccessful")


class TestWithdraw(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.url = cf.get('webauto', 'host')
        loginpage = LoginPageAction(self.driver, self.url)
        username = cf.get("webauto", "loginusername")
        password = cf.get("webauto", "loginpassword")
        loginpage.login(username, password)
        pass

    def tearDown(self):
        # driver.quit()
        pass

    def test_withdraw(self):
        withdraw=WithdrawAction(self.driver,self.url)
        available_amount=withdraw.withdraw()
        #read availableAmt
        self.assertEqual(available_amount[0]-int(cf.get('webauto','withdrawamount')), available_amount[1], "testSuccessful")

class TestInvest(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.url = cf.get('webauto', 'host')
        pass

    def tearDown(self):
        # driver.quit()
        pass

    def test_invest(self):
        # invest=InvestAction()
        loginpage = LoginPageAction(self.driver, self.url)
        newaccount_username = cf.get("webauto", "loginusername")
        newaccount_password = cf.get("webauto", "loginpassword")
        loginpage.login(newaccount_username, newaccount_password)
        #
        investpage=InvestPageAction(self.driver)
        #打开项目列表页面
        investpage.show_project()
        #选择一个项目进入投资页面
        investpage.select_project()
        #输入投资金额、提交、确认
        time.sleep(5)
        investpage.input_amount()
        investpage.click_submit()
        investpage.confirm()

        time.sleep(10)


class TestEnd(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        driver.quit()
        pass

    def test_end(self):
        pass
'''
问题：代码写的没问题，执行也成功了，但就是无法生成HTMLTestRunner的报告
其实这是编辑器搞得鬼，编辑器为了方便用户执行测试，都有一项功能，可以用编辑器来调用unittest或者nose来执行测试用例，这种情况下，执行的只是用例或者套件，而不是整个文件，写在main里的代码是不会被执行的！！自然无法生成测试报告
我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行
if __name__ == ‘__main__‘:
if __name__ == ‘python‘:
# 把main修改成自己的文件夹名就可以了

'''
if __name__ == '__main__':
    # 添加Suite
    print "oookk"
    def Suite():
        # 定义一个单元测试容器
        suiteTest = unittest.TestSuite()
        # 将测试用例加入到容器
        # suiteTest.addTest(TestLogin("test_login"))
        # suiteTest.addTest(TestLogin("testCase2"))
        ###########注册##########

        # suiteTest.addTest(TestRegister("test_register"))
        ###########开户##########

        # suiteTest.addTest(TestOpenAccount("test_openaccount"))
        ##########风险评估#######
        # suiteTest.addTest(TestRiskevaluate("test_riskevaluate"))

        # suiteTest.addTest(TestCharge("test_charge"))
        # suiteTest.addTest(TestWithdraw("test_withdraw"))
        ##########项目投资#######

        # suiteTest.addTest(TestInvest("test_invest"))
        # suiteTest.addTest(TestAccount("test_account"))
        # suiteTest.addTest(APITestCase("testCase3"))

        # suiteTest.addTest(TestEnd("test_end"))
        return suiteTest

    #确定生成报告的路径
    time_str=time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    filePath ="D:\\web_" + time_str + ".html"
    fp = file(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'web自动化测试报告',
        #description='详细测试用例结果',
        # tester=u"DKDtester"
        )
    #运行测试用例
    # count1 = 1
    # print " " + str(count1) + " times"
    # count1 += 1
    runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    fp.close()