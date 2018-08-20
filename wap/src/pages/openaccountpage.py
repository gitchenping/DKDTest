# coding=utf-8
"""页面基本操作方法：如open，input_username，input_password，click_submit"""
from selenium.webdriver.common.by import By

from myaccountpage import MyAccountPageAction
from wap.src.common import comm

import time

# 继承BasePage类
class OpenAccountAction(MyAccountPageAction):
    # 定位器，通过元素属性定位元素对象
    myaccountlink_loc = (By.LINK_TEXT, '我的账户')

    realname_loc=(By.ID,'realName')
    idcard_loc=(By.ID,'idCardNo')
    bankcard_loc=(By.ID,'bankCardNo')
    bankname_loc=(By.ID,'bankName')

    bankselect_loc=(By.CSS_SELECTOR,'li[data-value="105100000017"]')

    mobile_loc=(By.ID,'mobile')
    #下一步按钮
    nextstep_loc=(By.ID,'shPersonalRegister')

    #上传身份证
    # uploadimgfront_loc=(By.CSS_SELECTOR,'.idFront')
    uploadimgfront_loc = (By.CSS_SELECTOR, 'main>form:nth-of-type(1)')
    uploadimgback_loc = (By.CSS_SELECTOR, 'main>form:nth-of-type(2)')

    # uploadimgfront_loc=(By.XPATH,'//*[@id="uploadIdPage"]/main/form[1]/input')

    open_submit_loc=(By.LINK_TEXT,'提交开户')
    #上行短信验证码按钮
    SmsVerifybtn_loc=(By.ID,'sendSmsVerify')
    Smscodetext_loc=(By.ID,'smsCode')

    Smspassword_loc = (By.ID, 'password')
    Smsconfirmpassword_loc=(By.ID,'confirmPassword')

    #短信验证码弹窗
    Smsalert_loc=(By.LINK_TEXT,'知道了')

    #同意协议并注册
    agreeandsubmit_loc=(By.ID,'nextButton')


    #开户结果
    result_fail_id=(By.ID,'applyFail')
    result_success_id=(By.ID,'applySuccess')
    result_text="开户申请提交成功"
    miapage_href=(By.CSS_SELECTOR,'a[href="/project/list"]')


    #当前页面相对地址
    openaccount_url="/account/shAccount#open"


    # 开户页面打开
    def openaccount_web_open(self):
        self.find_element(*self.myaccountlink_loc).click()
        time.sleep(3)
        self.find_element(*self.accountlink_loc).click()

    def input_realname(self,realname):

        self.find_element(*self.realname_loc).send_keys(realname)

    def input_id(self,identify):
        self.find_element(*self.idcard_loc).send_keys(identify)

    def input_bankid(self,bankcardid):
        self.find_element(*self.bankcard_loc).send_keys(bankcardid)

    def select_bank(self):
        self.find_element(*self.bankname_loc).click()
        self.find_element(*self.bankselect_loc).click()
        time.sleep(1)

    def input_mobile(self,mobile):

        self.find_element(*self.mobile_loc).send_keys(mobile)

    def click_nextstepbtn(self):
        self.find_element(*self.nextstep_loc).click()

    def uploadimg(self,headimgpos,emblemimgpos):
        time.sleep(2)
        self.find_element(*self.uploadimgfront_loc).click()

        #上传肖像面
        posfront=headimgpos
        comm.winUpload(posfront)
        time.sleep(5)

        #上传国徽面
        self.find_element(*self.uploadimgback_loc).click()
        posback = emblemimgpos
        comm.winUpload(posback)
        time.sleep(5)

    def submit_openaccout(self):

        ele=self.find_element(*self.open_submit_loc)
        ele.click()

    def input_smsverifycode(self):
        self.find_element(*self.SmsVerifybtn_loc).click()
        self.find_element(*self.Smscodetext_loc).send_keys('1234')

    def input_smspassword(self):
        self.find_element(*self.Smspassword_loc).send_keys('999999')
        self.find_element(*self.Smsconfirmpassword_loc).send_keys('999999')

    def smsalert_click(self):
        time.sleep(2)
        self.find_element(*self.Smsalert_loc).click()

    def agree_protocol(self):
        self.find_element(*self.agreeandsubmit_loc).click()

    def openaccount_result(self):
        #true or false
        time.sleep(2)
        try:
             result_js='return '+'document.getElementById("applySuccess").innerText.includes("'+self.result_text+'")'
             # print result_js

        except:
            result_js = 'return ' + 'document.getElementById("applyFail").innerText.includes("' + self.result_text + '")'

        bool = self.driver.execute_script(result_js)

        return bool

    @classmethod
    def goback_mainpage(cls,driver):
        time.sleep(1)
        driver.find_element(*cls.miapage_href).click()