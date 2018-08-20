# coding=utf-8
"""页面基本操作方法：如open，input_username，input_password，click_submit"""
from selenium.webdriver.common.by import By
from basepage import BasePage

import random
import time
import ConfigParser
# import comm

cf=ConfigParser.ConfigParser()
cf.read('D:\\pycharm worker\\config.ini')

# 继承BasePage类
class RiskEvaluateAction(BasePage):
    # 定位器，通过元素属性定位元素对象
    myaccountlink_loc = (By.LINK_TEXT, '我的账户')
    risklink_loc=(By.LINK_TEXT,'立即评估')

    # evaluationsubmit_loc=(By.LINK_TEXT,'开始评估')

    riskprotcol_loc=(By.CSS_SELECTOR,'input[type="checkbox"]')
    answer_submit_loc=(By.LINK_TEXT,'提交问卷')

    risktype_loc=(By.CLASS_NAME,'userRiskType')

    #预设答案
    risktype="稳健型"
    question_list=['1c','2b','3c','4c','5c','6b','7b','8c','9c','10b','11c','12b']

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        # self.base_url = base_url

    def enter_riskevaluate(self):
        self.find_element(*self.myaccountlink_loc).click()
        self.find_element(*self.risklink_loc).click()
        time.sleep(2)
        # self.find_element(*self.evaluationsubmit_loc).click()
        pass

    def answer_question(self):
        for i in range(0,12):
            questionnaire_loc = (By.ID,self.question_list[i])
            self.find_element(*questionnaire_loc).click()
        #提交问卷
        self.find_element(*self.riskprotcol_loc).click()
        self.find_element(*self.answer_submit_loc).click()

    def getRiskUserType(self):
        time.sleep(3)
        risk_js="return "+"document.getElementsByClassName('userRiskType')[0].innerText.split('：')[1]"

        return self.driver.execute_script(risk_js)





