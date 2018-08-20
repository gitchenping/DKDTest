# -*- coding:utf-8 -*-
import webcfg
import time
from  Driver import driver

class MyaccountAction():
    def tradelog(self):

        # log=driver.find_element_by_xpath('//*[@id="main"]//table/tbody/tr[1]/td[4]').text
        log=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[4]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]').text
        # print driver.page_source
        print log
