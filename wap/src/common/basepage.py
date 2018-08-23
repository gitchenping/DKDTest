# coding=utf-8
"""基础类BasePage，封装所有页面都公用的方法，定义open,find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url"""
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.common.exceptions import NoAlertPresentException

class BasePage(object):

    website_url=""
    def __init__(self, selenium_driver, base_url):
        self.driver = selenium_driver
        self.base_url = base_url

    def _open(self, url):
        # 使用get打开访问链接地址
        self.driver.get(url)

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url)

    def save_websitedomain(self,driver):
        # 当前站点协议+域名
        urlstr = "return " + "document.location.origin"
        BasePage.website_url= driver.execute_script(urlstr)

    # 重写元素定位方法
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(loc))
            return self.driver.find_element(*loc)
        except TimeoutException:
            print u"%s 超过%s秒，页面中未能找到 %s 元素" % (self,20, loc)

    # 重写元素定位方法
    def find_elements(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(loc))
            return self.driver.find_elements(*loc)
        except TimeoutException:
            print u"%s 超过%s秒，页面中未能找到 %s 元素" % (self, 20, loc)

    #重写输入
    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError, e:
            raise e

    #判断元素是否存在
    def is_element_exist(self,selector):

        try:
            # self.driver.find_element(*selector)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(selector))
            return True
        # except NoSuchElementException :
        except TimeoutException:
            return False

    #判断有无windows弹窗
    def is_alert_exist(self):
        time.sleep(1)
        try:
            alert=self.driver.switch_to_alert()
            txt=alert.text
            alert.accept()
            return [True,txt]
        except NoAlertPresentException,e:
            return [False]

    #元素是否可点击
    def is_element_clickable(self,*loc):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
            return True
        except TimeoutException:
            return False

        # 判断元素是否存在(by,value)

    def wait_page_onload(self):
        js_str="return document.readyState"

        i=0
        while i<60:
            state = self.driver.execute_script(js_str)
            if state=="complete":
                break
            else:
                i=i+1
                time.sleep(1)




    #回退上一页
    def goback(self):
        self.driver.back()









