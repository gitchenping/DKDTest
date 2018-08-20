# coding=utf-8
"""页面基本操作方法：如open，input_username，input_password，click_submit"""
from selenium.webdriver.common.by import By
from basepage import BasePage
import time

# 继承BasePage类
class LoginPageAction(BasePage):
    # 定位器，通过元素属性定位元素对象
    accountlink_loc = (By.LINK_TEXT, '我的账户')
    username_loc=(By.NAME,'loginName')
    password_loc = (By.NAME, 'loginPwd')
    submit_loc = (By.CLASS_NAME, 'loginBtn')
    userid_loc = (By.ID, "usernameMain")
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    #ACCOUNT
    def click_account(self):
        self.find_element(*self.accountlink_loc).click()

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        #        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
     # 点击登录：调用send_keys对象，点击登录

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

        # 登录成功页面中的用户ID查找

    def show_userid(self):
        return self.find_element(*self.userid_loc).text


    def login(self,username,password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_submit()
        time.sleep(2)



