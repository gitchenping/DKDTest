# coding=utf-8
"""页面基本操作方法：如open，input_username，input_password，click_submit"""
from selenium.webdriver.common.by import By
from myaccountpage import MyAccountPageAction
import time

# 继承MyAccountPageAction类
class RiskEvaluateAction(MyAccountPageAction):
    # 定位器，通过元素属性定位元素对象

    # evaluationsubmit_loc=(By.LINK_TEXT,'开始评估')
    evaluationsubmit_loc = (By.CLASS_NAME, 'open')
    answer_submit_loc=(By.LINK_TEXT,'提交问卷')

    risktype_loc=(By.CLASS_NAME,'userRiskType')

    account_manage_loc=(By.LINK_TEXT,'账户管理')

    userrisktype_loc=(By.CLASS_NAME,'userRiskType')

    risk_path="/account/questionnaire"

    #预设答案
    risktype="保守型"
    riskprefrence_answer_list=['1a','2a','3a','4a','5a','6a','7a','8a','9a','10a','11a','12a']

    def is_on_withdrawpage(self):
        pathnamestr = "return " + "document.location.pathname"
        pathname = self.driver.execute_script(pathnamestr)

        if pathname == self.risk_path:
            return True
        else:
            return False

    def answer_question(self,riskprefrence=None):
        if riskprefrence==None:
            riskprefrence_answer=self.riskprefrence_answer_list
        else:
            riskprefrence_answer=riskprefrence
            for i in range(0,12):
                questionnaire_loc = (By.ID,riskprefrence_answer[i])
                self.find_element(*questionnaire_loc).click()

    def click_questionnaire_submitbtn(self):

        #提交问卷
        self.find_element(*self.answer_submit_loc).click()

    def getRiskUserType(self):

        risk_js="return "+"document.getElementsByClassName('userRiskType')[0].innerText.split('：')[1]"

        return self.driver.execute_script(risk_js)

    def enter_questionare(self):
        self.find_element(*self.risklink_loc).click()
        # print "begin"
        # self.wait_page_onload()
        time.sleep(3)
        ele=self.find_element(*self.evaluationsubmit_loc)
        ele.click()

        # js_str=r"document.getElementsByClassName('open')[0].click();"
        # self.driver.execute_script(js_str)
        # print "ele object="+str(ele)
        # print "end"

    #返回用户风险偏好
    def get_userrisktype(self):
        #提取标签之间的文本，忽略标签内部嵌套的标签
        risktype=self.find_element(*self.userrisktype_loc).text
        type=risktype.split('：')
        # print type
        return type[1]


