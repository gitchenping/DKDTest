# -*- coding:utf-8 -*-

import time
import os

from src.common import HTMLTestRunnerCN
from suit import suite_new,suite_stock


if __name__ == '__main__':
    # 添加Suite
    print "run start...."


    #存量用户和新用户用例切换
    suiteTest=suite_stock()
    # suiteTest=suite_new()


    #确定生成报告的路径
    time_str=time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(__file__)) + "\\report\\"
    filename ="wap_" + time_str + ".html"
    filefullpath=file_path+filename

    fp = file(filefullpath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'wap自动化测试报告',
        #description='详细测试用例结果',
        # tester=u"DKDtester"
        )
    #运行测试用例

    runner.run(suiteTest)
    # 关闭文件，否则会无法生成文件
    fp.close()
    print "run complete!"

