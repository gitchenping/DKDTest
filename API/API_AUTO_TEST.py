# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunnerCN
import time

# class TestLogin(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def test_login(self):
#         global TOKEN
#         result=LogIn().login_correct()
#
#
#
#         self.assertEqual("1","1")
#         TOKEN = result['token']
test_dir='./interface'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*.py')
if __name__ == '__main__':
    # 添加Suite
    print "run start...."
    # def Suite():
    #     # 定义一个单元测试容器
    #     suiteTest = unittest.TestSuite()
    #     # 将测试用例加入到容器
    #     # suiteTest.addTest(TestLogin("test_login"))
    #     # suiteTest.addTest(TestLogin("testCase2"))
    #
    #     return suiteTest

    #确定生成报告的路径
    time_str=time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
    filePath ="D:\\NewPythonWorkplace\\API\\report\\api_" + time_str + ".html"
    fp = file(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'API自动化测试结果报告',
        #description='详细测试用例结果',
        tester=u"DKDtester"
        )
    #运行测试用例

    # runner.run(Suite())
    runner.run(discover)
    # 关闭文件，否则会无法生成文件
    fp.close()

    print "run complete!"