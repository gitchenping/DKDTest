# -*- coding:utf-8 -*-
import webcfg
import time
from  Driver import driver
from selenium.webdriver.common.by import By
from basepage import BasePage

import  ConfigParser
cf=ConfigParser.ConfigParser()
cf.read('D:\\NewPythonWorkplace\\config.ini')

class ChargeAction(BasePage):

    # 定位器，通过元素属性定位元素对象

    #可用余额
    amountAvailable=(By.ID,'availableAmt')

    #充值页
    chargePage_loc=(By.ID,'chargePage')
    chargeAmount_loc=(By.ID,'chargeAmount')

    chargeEvent_loc=(By.LINK_TEXT,'充值到资金账户')

    chargeTip_loc=(By.CLASS_NAME,'neverShow')
    chargeConfirm_loc=(By.ID,'chargeConfirm')

    chargeReturn_loc=(By.ID,'popupCancel')

    def amountRecord(self):
        amount=self.find_element(*self.amountAvailable).text
        return amount.replace(',','').split('.')[0]



    def charge(self):
        #read current available amount
        available_amount_before_charge=self.amountRecord()

        #charge
        self.find_element(*self.chargePage_loc).click()
        self.find_element(*self.chargeAmount_loc).send_keys(cf.get('webauto','chargeamount'))
        self.find_element(*self.chargeEvent_loc).click()

        #charge tip
        # self.find_element(*self.chargeTip_loc)
        self.find_element(*self.chargeConfirm_loc).click()

        #charge result
        self.find_element(*self.chargeReturn_loc).click()

        #关闭新打开页
        handles=driver.window_handles
        for handle in handles:
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
                driver.close()
                break
        driver.switch_to.window(handles[0])

        time.sleep(5)

        #amount after charge
        available_amount_after_charge=self.amountRecord()
        available_amount=[int(available_amount_before_charge),int(available_amount_after_charge)]
        return available_amount

