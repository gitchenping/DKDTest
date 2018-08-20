# -*- coding:utf-8 -*-
import webcfg
import time
# from Driver import driver
from mouse import mouse_click
from basepage import BasePage
from selenium.webdriver.common.by import By



class InvestPageAction(BasePage):
    # 定位器，通过元素属性定位元素对象
    amount_loc = (By.ID, 'inputAmount')
    investbtn_loc = (By.CLASS_NAME, 'invest')
    riskwarn_loc=(By.ID,'investPop3')
    riskwarncheckbox_loc=(By.ID,'agreeInvest3')

    investconfirmbtn_loc = (By.LINK_TEXT, '确认投资')
    cancelbtn_loc=(By.LINK_TEXT,'取消')

    link_loc=(By.LINK_TEXT,'确认订单')
    check_loc=(By.XPATH,"//*[@type='checkbox']")

    projectlist_loc=(By.ID,'nav_list')



    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    def show_project(self):
        self.find_element(*self.projectlist_loc).click()
        time.sleep(10)
    def select_project(self):
        # xtemp = webcfg.X_init
        # ytemp = webcfg.Y_init
        #
        #
        # height = 1.1 * webcfg.offset
        # 投标失败的情况，待改，考虑已投满的情况
        # for i in range(0,10):
        #     js = "document.documentElement.scrollTop = " + str(height*i)
        #     driver.execute_script(js)
        #     time.sleep(5)
        #     mouse_click(xtemp,ytemp)
        #
        #     time.sleep(3)
        #     #
        #     handles = driver.window_handles
        #     for handle in handles:
        #         if handle != driver.current_window_handle:
        #             driver.switch_to.window(handle)
        #             break
        #     investpage.input_amount(webcfg.invest_amount)
        #     investpage.click_submit()
        #
        #     time.sleep(3)
        #     investpage.confirm()
        #
        #     if investpage.is_alert_exits():
        #         self.driver.switch_to_alert().dismiss()
        #         self.driver.close()
        #         self.driver.switch_to.window(handles[0])
        #     else:
        #         break
        # 使用js 找到如下innerText的可投资项目
        # ["剩余额度 95,100元", "", "投资中", ""]
        js_function = ('i=0;function invest(){ var project = document.getElementsByClassName("table-project");'
                       'var tbody = project[0].getElementsByTagName("tbody");var tr = tbody[0].getElementsByTagName("tr");'
                       'var i = 0;for (i=0;i < 10;i++){var td=tr[i].getElementsByTagName("td");var available_amount_str=td'
                       '[5].innerText.split("\\n");if (available_amount_str[2] == "投资中" ){var start=available_amount_str'
                       '[0].indexOf("度");var end=available_amount_str[0].indexOf("元");var amount_str=available_amount_str'
                       '[0].substring(start+1,end).replace(",", "");''var amount_int=Number(amount_str);if (amount_int>100)'
                       '{td[5].getElementsByTagName("div")[0].click();break;}}}}'
                       'invest();if(i==10){console.log("there are not any largeScale project to invest!"); '
                       'document.getElementById("smallScale").click();setTimeout("invest()",5000);'
                       'if(i==10){console.log("there are not any smallScale project to invest!");}}'
                       )
        # print js_function
        self.driver.execute_script(js_function)


    # 调用send_keys对象，输入投资金额
    def input_amount(self):
        #        self.find_element(*self.username_loc).clear()
        #项目投资页新打开的窗口，窗口句柄指向新页面
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                # driver.close()
                break
        #首先判断起投金额
        js_amount_start="return "+"document.getElementById("+"'"+self.amount_loc[1]+"'"+").placeholder"
        amount_startstr=self.driver.execute_script(js_amount_start)

        index=amount_startstr.find(u'元')
        amount=amount_startstr[0:index]


        # self.driver.find_element_by_id("inputAmount").send_keys(amount)
        self.find_element(*self.amount_loc).send_keys(amount)


    # 调用send_keys对象，点击提交
    def click_submit(self):

        self.find_element(*self.investbtn_loc).click()
        time.sleep(1)
        #风险提示处理
        if self.is_element_exits(self.riskwarn_loc):
            time.sleep(1)
            if not self.find_element(*self.riskwarncheckbox_loc).is_selected():
                self.find_element(*self.riskwarncheckbox_loc).click()
            #确定
            self.find_element(*self.investconfirmbtn_loc).click()



    #确认订单
    def confirm(self):
       #勾选checkbox
       if not self.find_element(*self.check_loc).is_selected():
           self.find_element(*self.check_loc).click()

        #点击确认
       self.find_element(*self.link_loc).click()




