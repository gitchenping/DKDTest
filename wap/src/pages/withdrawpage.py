# coding=utf-8

from selenium.webdriver.common.by import By
import os
import sys
import time

# from wap.src.common.basepage import BasePage
from myaccountpage import MyAccountPageAction

class WithdrawPageAction(MyAccountPageAction):
    # 定位器，通过元素属性定位元素对象
    # myaccountlink_loc = (By.LINK_TEXT, '我的账户')
    # withdrawlink_loc = (By.LINK_TEXT, '提现')

    commonwithdrabtn_loc=(By.LINK_TEXT,'大额提现')

    #可提取金额
    availableWithdrawAmt=(By.CLASS_NAME,'availableWithdrawAmt')


    #实时提现
    #提现金额输入框
    withdrawamt_loc=(By.CSS_SELECTOR,'#realTimeWithdraw>div>input')
    #提现到银行卡按钮
    withdrawtobankcard_loc=(By.CSS_SELECTOR,'#realTimeWithdraw>div:nth-of-type(2)+a')

    #普通提现
    commonwithdrawamt_loc=(By.CSS_SELECTOR,'#commonWithdraw>div>input')
    commonwithdrawtobankcard_loc=(By.CSS_SELECTOR,'#commonWithdraw>div:nth-of-type(2)+a')


    #交易密码
    password=(By.ID,'password')

    # 账户view
    accountview_loc = (By.CSS_SELECTOR, 'a[href="/account/overview"]')

    #提现页面相对位置
    withdraw_path="/withdraw/withdraw"


    #提现金额输入
    def input_withdrawamt(self,amount,real=True):
        if real:
            self.send_keys(amount,*self.withdrawamt_loc)
        else:
            self.send_keys(amount, *self.commonwithdrawamt_loc)


    # 提现资金到账户按钮
    def click_withdrawtoaccountbtn(self,real=True):
        time.sleep(1)
        if real:
            self.find_element(*self.withdrawtobankcard_loc).click()
        else:
            self.find_element(*self.commonwithdrawtobankcard_loc).click()

    def is_on_withdrawpage(self):
        pathnamestr = "return " + "document.location.pathname"
        pathname = self.driver.execute_script(pathnamestr)

        if pathname == self.withdraw_path:
            return True
        else:
            return False

    #当前可提取金额
    def get_todayavailableamt(self):
        amtstr= self.find_element(*self.availableWithdrawAmt).text
        return float(amtstr.replace(',',''))

    def enter_commonwithdrawpage(self):

        ele=self.find_element(*self.commonwithdrabtn_loc)
        ele.click()


















