# -*- coding:utf-8 -*-
import base64
import hashlib
import requests
import time

secret='10f23d3c01b342c1958659f6aedc846a'



import unittest
import HTMLTestRunnerCN

from python import TestDemo
from android import TestDemo2

if __name__ == '__main__':
    # unittest.main()
    def Suite():
        suiteTest = unittest.TestSuite()
        suiteTest.addTest(TestDemo("test_case_A"))
        suiteTest.addTest(TestDemo2("test_case_B"))
        # suiteTest.addTest(TestDemo("test_case_C"))
        return suiteTest
        # 确定生成报告的路径
    time_str = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    filePath = "D:\\web_" + time_str + ".html"
    fp = file(filePath, 'wb')
        # 生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'web自动化测试报告',
            # description='详细测试用例结果',
            # tester=u"DKDtester"
        )


    runner.run(Suite())
