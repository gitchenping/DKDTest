# coding=utf-8
"""基础类BasePage，封装所有页面都公用的方法，定义open,find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import time

from APP.src.common.uihelper import Driver

from APP.src.common.uihelper import UIhelper

from appium.webdriver.common.mobileby import MobileBy

class BasePage(object):


    def __init__(self):

        self.driver = Driver().getDriver()
        pass

    # 重写元素定位方法
    def findElement(self, loc):
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
            print u"%s 超时，页面中未能找到 %s 元素" % (self, loc)

    def findElements(self,loc):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(loc))
            return self.driver.find_elements(*loc)
        except TimeoutException:
            print u"%s 超时，页面中未能找到 %s 元素" % (self, loc)

    def comfindElement(self, controlInfo,waittime=10):
        element = ""
        for i in range(0,waittime):
             time.sleep(1)
             try:
                    if (controlInfo.startswith("//")):
                         element = self.driver.find_element_by_xpath(controlInfo)
                    elif (":id/" in controlInfo or ":string/" in controlInfo):
                         element = self.driver.find_element_by_id(controlInfo)
                    else:
                         # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
                        try:
                            element = self.driver.find_element_by_name(controlInfo)
                        except:
                            # logging.logger.logDebug("Cannot find the element by id, try class name")
                             # 如果通过名称不能找到，则通过class name查找
                            element = self.driver.find_elements_by_class_name(controlInfo)
                    return element
             except:
                    continue
        raise Exception("can't find %s in %d seconds"% (controlInfo,waittime))



    #重写输入
    def send_keys(self, controlInfo,value, waittime=10):
        try:
            self.comfindElement(controlInfo,waittime).clear()
            self.comfindElement(controlInfo,waittime).send_keys(value)
        except AttributeError, e:
            raise e

    #判断元素是否存在(by,value)
    def is_element_exist(self,selector):
        if (":id/" in selector or ":string/" in selector):
            selector = (MobileBy.ID, selector)

        try:
            # self.driver.find_element(*selector)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
            return True
        except NoSuchElementException :
            return False

    #判断有无windows弹窗
    def is_alert_exist(self):
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


    #返回元素的绝对位置及 大小（宽、高）
    def getElementsize(self,controlInfo):
        # 获取元素的左上角坐标
        element=self.comfindElement(controlInfo)
        x = element.location['x']
        y = element.location['y']
        # 获取元素的宽、高
        width = element.size['width']
        height = element.size['height']

        return [x,y,width,height]


    def mock_comfindElement(self, controlInfo,waittime=10):
        element = ""
        for i in range(0,waittime):
             time.sleep(1)
             try:
                    if (controlInfo.startswith("//")):
                         print "find element by xpath"
                    elif (":id/" in controlInfo or ":string/" in controlInfo):
                         print "find element by id"
                    else:
                         # 剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
                        try:
                            # element = self.driver.find_element_by_name(controlInfo)
                            print "通过名字查找"+controlInfo
                        except:
                            # logging.logger.logDebug("Cannot find the element by id, try class name")
                             # 如果通过名称不能找到，则通过class name查找
                            element = self.driver.find_elements_by_class_name(controlInfo)
                    return element
             except:
                    continue
        raise Exception("can't find %s in %d seconds"% (controlInfo,waittime))

    def clear_text(self,ele):
        '''清除输入文本框内容'''
        ele.click()#激活该文本框
        content=ele.get_attribute('text')

        #光标移动到输入框最右边
        self.driver.keyevent(123)
        for i in range(0,len(content)):
            self.driver.keyevent(67)#delete键

        pass

    def get_eletext(self,element_pos):
        ele=self.comfindElement(element_pos)

        return ele.text

    #模拟按键
    def keyaction(self,intnum):
        #1、KEYCODE_BACK 返回键 4
        #2、KEYCODE_ENTER 回车键 66
        #3、KEYCODE_TAB Tab键 61

        self.driver.keyevent(intnum)
