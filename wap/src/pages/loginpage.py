# coding=utf-8

from selenium.webdriver.common.by import By
import os
import sys
import time
# toppath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# sys.path.append(toppath)
# from common.basepage import BasePage


from wap.src.common.basepage import BasePage

# 继承BasePage类
class LoginPageAction(BasePage):

    # 定位器，通过元素属性定位元素对象
    username_loc=(By.ID,'UserName')
    password_loc = (By.ID, 'Password')
    submit_loc = (By.CLASS_NAME, 'btn')

    myaccountlink_loc = (By.LINK_TEXT, "我的账户")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        time.sleep(1)
        # self.find_element(*self.username_loc).clear()
        # self.find_element(*self.username_loc).send_keys(username)
        self.send_keys(username,*self.username_loc)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.send_keys(password, *self.password_loc)

    # 点击登录
    def click_submitbtn(self):
        self.find_element(*self.submit_loc).click()

    def is_myaccoutlink_exist(self):
        if self.is_element_exist(self.myaccountlink_loc):

            return True
        else:
            return False








