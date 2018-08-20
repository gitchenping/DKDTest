# -*- coding:utf-8 -*-

import unittest
import time
import os
# import HTMLTestRunnerCN
from src.common import HTMLTestRunnerCN

from cases.login import TestLogin
from cases.openaccount import TestOpenAccount

if __name__ == '__main__':
    # 添加Suite
    print "run start...."

    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()

    # 将测试用例加入到容器

    # for user in userlist:


    # suiteTest.addTest(TestLogin("test_login_wrongpassword"))
    # suiteTest.addTest(TestLogin("test_login_success"))

    suiteTest.addTest(TestOpenAccount("test_openaccount_success"))




    #确定生成报告的路径
    time_str=time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(__file__)) + "\\report\\"
    filename ="app_" + time_str + ".html"
    filefullpath=file_path+filename

    fp = file(filefullpath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'app自动化测试报告',
        #description='详细测试用例结果',
        # tester=u"DKDtester"
        )
    #运行测试用例

    runner.run(suiteTest)
    # 关闭文件，否则会无法生成文件
    fp.close()
    print "run complete!"

