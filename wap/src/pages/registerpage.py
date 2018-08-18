# coding=utf-8

import os
import sys
import time

from wap.src.common.basepage import BasePage
from selenium.webdriver.common.by import By
from wap.src.common import comm


class RegisterPageAction(BasePage):

    # 定位器，通过元素属性定位元素对象
    registerlink_loc = (By.LINK_TEXT, '免费注册')
    #手机号输入框
    registername_loc=(By.NAME,'mobile')

    #图片验证码输入框
    imgcodetext_loc = (By.NAME, 'imageVerifyCode')
    #图片验证码
    imgrefresh_loc=(By.CLASS_NAME,'kaptcha')

    #短信验证码
    msgcodetext_loc = (By.NAME, "verifyCode")
    msgget_loc=(By.LINK_TEXT,'获取短信验证码')

    #注册密码
    password_loc = (By.NAME, 'password')

    #注册按钮
    submit_loc=(By.LINK_TEXT,'注册')

    #注册成功页
    register_back_loc=(By.CSS_SELECTOR,'a[href="/project/list"]')

    #结果页文案
    register_text="registerSuccess"



    invest_path = "/project/list"
    registerpage_path="/user/register"


    #默认注册入口页(登录页面)
    def click_reigisterbtn(self):
        self.find_element(*self.registerlink_loc).click()

    # 是否在注册页面
    def is_on_registerpage(self):
        pathnamestr = "return " + "document.location.pathname"
        pathname = self.driver.execute_script(pathnamestr)

        if pathname == self.registerpage_path:
            return True
        else:
            return False

    #从其他页面直接进入注册页
    def enter_registerpage(self):
        urlstr = self.website_url
        # url=self.driver.execute_script(urlstr)
        registerurl = urlstr + self.registerpage_path
        js = 'location.href=' + '"' + registerurl + '"'
        self.driver.execute_script(js)



    # 输入密码：调用send_keys对象，输入注册手机号
    def input_registername(self,registername):

        # self.send_keys(registername,*self.registername_loc)
        self.find_element(*self.registername_loc).send_keys(registername)

    # 点击注册
    def click_registerbtn(self):
        self.find_element(*self.submit_loc).click()

    def click_imgrefreshbtn(self):
        self.find_element(*self.imgrefresh_loc).click()

    def clear_imgcodetext(self):
        self.find_element(*self.imgcodetext_loc).clear()

    # def clcik_msgget

    def is_getmsgcode_send(self):
        if self.is_element_clickable(*self.msgget_loc):
            self.find_element(*self.msgget_loc).click()
            return True
        else:
            return False
        # return False

    #获取短信验证码
    def get_msgverifycode(self,tel):
        sql="select verify from sp_mobile_verify_code where mobile = "+tel+" order by id desc limit 0,1 ;"
        conn = comm.DB()
        res = conn.dbsearch(sql)
        # print res[0][0]
        # self.find_element(*self.msgcodetext_loc).send_keys(res[0][0])

        return res[0][0]

    # 输入短信验证码
    def input_msgverifycode(self,msgverifycode):

        # print res[0][0]
        self.find_element(*self.msgcodetext_loc).send_keys(msgverifycode)


    def input_imgverifycode(self,imgverifycode):

        self.send_keys(imgverifycode, *self.imgcodetext_loc)
        pass

    def input_registerpwd(self,registerpassword):

        self.send_keys(registerpassword, *self.password_loc)
        pass


    def get_imgverifycode(self,imgsavepath,imgcodesavepath):

        imageelemnt = self.find_element(*self.imgrefresh_loc)
        location = imageelemnt.location  # 获取验证码图片x,y轴坐标
        size = imageelemnt.size  # 获取验证码的长宽

        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标

        text=""

        self.driver.save_screenshot(imgsavepath)

        text=comm.imgverifycode_recongnise(imgsavepath,imgcodesavepath,rangle)

        # 长度判断，非5个字符，肯定不对
        if len(text) < 5 or len(text) >= 6 or not text.isalnum():
            self.find_element(*self.imgrefresh_loc).click()
            return ""

        else:
            #     print text
            return text



    def check_imgverifycode_right(self):
        if self.is_getmsgcode_send():
            # print "click is ok"
            # 如果有弹框，说明验证码错误
            # 点击获取短信验证码（此步校验图片验证码是否识别正确）
            time.sleep(2)
            alert = self.is_alert_exist()
            if alert[0]:
                self.clear_imgcodetext()
                self.click_imgrefreshbtn()
                return False
            else:

                return True

        else:
            # 短信验证码不可点击
            print "短信验证码发送失败,脚本无法校验"
            sys.exit(0)
            pass

    #回到默认首页
    @classmethod
    def goback(cls):
        cls.find_element(*cls.register_back_loc).click()

    @classmethod
    def backto_investpage(cls, driver):
        #延时，若马上跳转，可能为非登录状态
        time.sleep(5)
        urlstr = cls.website_url

        # myaccounturl=urlstr+self.path
        myaccounturl = urlstr + cls.invest_path

        js = 'location.href=' + '"' + myaccounturl + '"'
        # self.driver.execute_script(js)
        driver.execute_script(js)

    #返回一个列表
    def get_regiseterresult(self,driver):
        result_js="return document.getElementById('"+self.register_text+"').innerText.split('\\n')"
        # print result_js
        text=driver.execute_script(result_js)
        return text


