# coding=utf-8

from selenium.webdriver.common.by import By
import os
import sys
import time

from wap.src.common.basepage import BasePage

class MyAccountPageAction(BasePage):

    # 定位器，通过元素属性定位元素对象
    myaccountlink_loc = (By.LINK_TEXT, '我的账户')
    wantinvestlink_loc=(By.LINK_TEXT,'我要投资')

    risklink_loc = (By.LINK_TEXT, '< 风险承受能力评估 >')

    chargelink_loc = (By.LINK_TEXT, '充值')
    withdrawlink_loc=(By.LINK_TEXT, '提现')

    # shaccountlink_loc=(By.LINK_TEXT, '资金账户')
    shaccountlink_loc=(By.CSS_SELECTOR,'a[data-href="/account/shAccount"]')
    # shaccountlink_loc = (By.CSS_SELECTOR, 'a[href="/account/shAccount#open"]')

    #未开户提示弹窗
    noaccount_popalert_loc=(By.CSS_SELECTOR,'p[class="text-center"]')
    noaccount_popalertclose_loc=(By.CSS_SELECTOR,'a[class="popup-close"]')

    # 账户view
    accountview_loc = (By.CSS_SELECTOR, 'a[href="/account/overview"]')

    #交易明细
    traderecord_loc=(By.CSS_SELECTOR,'a[href="/manage/transRecord"]')


    #我的账户页面相对地址
    path="/account/overview"

    invest_path="/project/list"


    #重写父类__init__方法，进入各功能页面总入口页
    def __init__(self,selenium_driver):
        self.driver=selenium_driver
        # self.driver.find_element(*self.myaccountlink_loc).click()
        self.find_element(*self.myaccountlink_loc).click()
        pass


    #获取账户金额，返回总资产、可用余额
    def get_accountamt(self):
        total_js = "document.getElementsByClassName('total')[0].innerText.substring(6,).replace(/,/g,'')"
        js = "return " + total_js
        totalamt = self.driver.execute_script(js)

        remain_js = "document.getElementsByClassName('remain')[0].innerText.substring(7,).replace(/,/g,'')"
        js = "return " + remain_js
        remainamt = self.driver.execute_script(js)

        #保留两位小数
        return [float(totalamt), float(remainamt)]

    def click_wantinvestbtn(self):
        self.find_element(*self.wantinvestlink_loc).click()


    def click_chargebtn(self):
        time.sleep(2)

        self.find_element(*self.chargelink_loc).click()


    def click_withdrawbtn(self):
        time.sleep(1)

        self.find_element(*self.withdrawlink_loc).click()
        time.sleep(1)
        self.wait_page_onload()


    def click_accountbtn(self):
        time.sleep(2)
        self.find_element(*self.shaccountlink_loc).click()

    def click_traderecordbtn(self):

        self.find_element(*self.traderecord_loc).click()



    #（从项目投资页进入）我的账户页
    def click_myaccountlink(self):
        self.find_element(*self.myaccountlink_loc).click()


    #登录后，从其他页面跳转进入我的账户页
    # @classmethod
    def enter_myaccountpage(self):

        # host="return "+"document.location.host"
        # protocol="return "+"document.location.protocol"
        urlstr=self.website_url
        # urlstr = cls.website_url

        myaccounturl=urlstr+self.path
        # myaccounturl = urlstr + cls.path

        js='location.href='+'"'+myaccounturl+'"'
        # self.driver.execute_script(js)
        self.driver.execute_script(js)

    @classmethod
    def backto_investpage(cls,driver):
        urlstr = cls.website_url

        # myaccounturl=urlstr+self.path
        myaccounturl = urlstr + cls.invest_path

        js = 'location.href=' + '"' + myaccounturl + '"'
        # self.driver.execute_script(js)
        driver.execute_script(js)


    #是否在我的账户-充值提现投资 入口页
    def is_on_myaccountpage(self):
        pathnamestr="return "+"document.location.pathname"
        pathname=self.driver.execute_script(pathnamestr)

        if pathname ==self.path:
            return True
        else:
            return False

    #未开户充值提现弹窗提示
    def is_noaccountpopalert_exist(self):
        if self.is_element_exist(self.noaccount_popalert_loc):
            return True
        else:
            return False

    def noaccount_alert(self):

        if self.is_noaccountpopalert_exist():
            #返回文本
            text=self.find_element(*self.noaccount_popalert_loc).text
            self.find_element(*self.noaccount_popalertclose_loc).click()
            return text

        else:
            return ""



