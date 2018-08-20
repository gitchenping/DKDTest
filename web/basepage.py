# coding=utf-8
"""基础类BasePage，封装所有页面都公用的方法，定义open,find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class BasePage(object):
    def __init__(self, selenium_driver, base_url):
        self.driver = selenium_driver
        self.base_url = base_url

    def _open(self, url):
        # 使用get打开访问链接地址
        self.driver.get(url)

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url)

        # 重写元素定位方法

    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AttributeError:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)


    #页面元素是否存在
    def is_element_exits(self, selector):

        try:
            self.driver.find_element(*selector)
            return True
        except NoSuchElementException:
            return False

    def is_alert_exits(self):
        try:
            alert=self.driver.switch_to_alert()
            return True
        except NoAlertPresentException,e:
            return False






