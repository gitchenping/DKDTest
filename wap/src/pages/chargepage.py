# coding=utf-8

import os
import sys
import time

from selenium.webdriver.common.by import By


from myaccountpage import MyAccountPageAction

class ChargePageAction(MyAccountPageAction):
    # 定位器，通过元素属性定位元素对象
    myaccountlink_loc = (By.LINK_TEXT, '我的账户')
    chargelink_loc = (By.LINK_TEXT, '充值')
    daikouchargelink_loc=(By.LINK_TEXT,'代扣充值')
    bankchargelink_loc=(By.LINK_TEXT,'转账充值')

    chargeconfirmlink_loc=(By.LINK_TEXT,'确认充值')
    #确认充值弹窗
    chargeconfirmpop_loc=(By.ID,'chargeRulePop')

    chargetobankcard_loc=(By.LINK_TEXT,'充值到资金账户')

    amount_loc=(By.NAME,'amount')

    #交易密码
    password=(By.ID,'password')
    #懒猫页面确认支付按钮
    agreeprotocol_loc=(By.ID,'nextButton')


    investsuccess_text="充值申请提交成功"

    # 账户信息
    # accountview_loc = (By.CSS_SELECTOR, 'a[href="/account/overview"]')
    accountName_loc=(By.CLASS_NAME,"accountName")
    idCardCode_loc=(By.CLASS_NAME,"idCardCode")
    accountNo_loc=(By.CLASS_NAME,"accountNo")
    bank_loc=(By.CLASS_NAME,"bank")
    # bankName_loc=(By.CLASS_NAME,"bankName")
    bankName_loc=(By.CSS_SELECTOR,"td[class='bankName']")
    province_loc=(By.CLASS_NAME,"province")
    bankaccountinfolist_loc=[accountName_loc,idCardCode_loc,accountNo_loc,bank_loc,bankName_loc,province_loc]

    #当前页面相对地址
    charge_path="/charge/charge"


    #进入代扣充值页面、输入充值金额
    def input_chargeamt(self,amount):

        #进入代扣充值页面
        self.find_element(*self.daikouchargelink_loc).click()
        # self.find_element(*self.amount_loc).send_keys(amount)
        self.send_keys(amount,*self.amount_loc)


    #充值资金到账户
    def click_chargetoaccount(self):

        self.find_element(*self.chargetobankcard_loc).click()
        # if self.is_element_exist(self.chargeconfirmpop_loc):
        #     self.find_element(*self.chargeconfirmlink_loc).click()

    # 充值确认
    def is_chargeconfirm_exist(self):

        if self.is_element_exist(self.chargeconfirmpop_loc):
            self.find_element(*self.chargeconfirmlink_loc).click()
            return True
        else:
            return False

    #同意上行协议并支付
    def input_TradingPassword(self,password):
        self.find_element(*self.password).send_keys(password)
        self.find_element(*self.agreeprotocol_loc).click()


    #是否在我的账户-充值页(默认转账充值页)
    def is_on_chargepage(self):
        pathnamestr="return "+"document.location.pathname"
        pathname=self.driver.execute_script(pathnamestr)

        if pathname ==self.charge_path:
            return True
        else:
            return False

    def get_bankaccountinfo(self):

        bankaccountinfo={}

        # length=len(self.bankaccountinfolist_loc)
        for loc in self.bankaccountinfolist_loc:
            key=loc[1]
            if key=="td[class='bankName']":
                key="bankName"
            value=self.find_element(*loc).text
            bankaccountinfo[key]=value
            time.sleep(1)
            # print loc

        return bankaccountinfo











