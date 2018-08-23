# coding=utf-8

from selenium.webdriver.common.by import By
import os
import sys
import time

from wap.src.common.basepage import BasePage
from myaccountpage import MyAccountPageAction

class TradeDetailPageAction(MyAccountPageAction):

    # 定位器，通过元素属性定位元素对象
    # 重写父类__init__方法，进入各功能页面总入口页

    #
    record_loc=(By.CLASS_NAME,'record')

    #我的账户页面相对地址
    path="/account/overview"

    record_path="/manage/transRecord"

    def __init__(self,selenium_driver):
        self.driver=selenium_driver
        # self.driver.find_element(*self.myaccountlink_loc).click()
        self.click_traderecordbtn()
        pass


    #获取账户金额，返回总资产、可用余额
    def get_traderecord(self,type=None):

        ele=self.find_elements(*self.record_loc)
        info_list=ele[0].text.split("\n")

        if type == "charge" and info_list[0]==u"充值":

            pass
        elif type=="withdraw" and info_list[0]==u"提现":

            pass
        else:
            return ""

        tradeamt=float(info_list[2].replace(" ",""))

        return [tradeamt,info_list[3]]

        # while i<len(ele):
        #
        #     record_list=ele[i].text
        #     if type=="charge" :
        #
        #          pass
        #     elif type=="withdraw":
        #
        #          pass
        #     elif type=="invest":
        #          pass
        #     elif type=="rateback":
        #         pass
        #     else:
        #         pass
        #     i=i+1
        #返回交易金额和日期
        # return [,]


