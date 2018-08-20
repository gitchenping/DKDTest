# -*- coding:utf-8 -*-
import webcfg
import time
from  Driver import driver

class WithdrawAction():
    def withdraw(self):
        #read current available amount
        available_money=driver.find_element_by_id("availableAmt").text

        #charge
        driver.find_element_by_id("withdrawPage").click()
        time.sleep(3)
        driver.find_element_by_id("withdrawAmount").send_keys(webcfg.withdraw_money)
        time.sleep(3)
        driver.find_element_by_class_name("withdrawEvent").click()
        time.sleep(3)

        #
        handles=driver.window_handles
        for handle in handles:
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
                driver.close()
                break
        driver.switch_to.window(handles[0])
        driver.find_element_by_id("nav_account").click()

        # print driver.current_window_handle
        time.sleep(5)

        #read available amount after charge
        available_money_charge = driver.find_element_by_id("availableAmt").text

