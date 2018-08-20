# coding=utf-8
"""页面基本操作方法：如open，input_username，input_password，click_submit"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from basepage import BasePage
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import random
import time
import ConfigParser
import pymysql

import comm

cf=ConfigParser.ConfigParser()
cf.read('D:\\NewPythonWorkplace\\config.ini')

# from pytesseract import image_to_string
import pytesseract

class Person():
    def __init__(self):
        self.prefix_phone=['134','135','138','139','151','152','157',\
                           '158','188','156','170']
        self.lastname=[u'赵',u'钱',u'孙',u'李',u'周',u'吴']
        self.firstname=[u'孟德',u'公明',u'玄德',u'子',u'浩然',u'正德']


        self.weight=[7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        self.id_verifycode={'0':'1','1':'0','2':'X','3':'9', \
                            '4':'8','5':'7','6':'6','7':'5','8':'4','9':'3','10':'2'}
        pass
#手机号
    def get_phone_number(self):
        index=random.randint(0,len(self.prefix_phone)-1)
        return self.prefix_phone[index] + "".join(random.choice("0123456789") for i in range(8))
#姓名
    def return_new_name(self):
        index_last = random.randint(0, len(self.lastname) - 1)
        index_first=random.randint(0, len(self.firstname) - 1)
        return self.lastname[index_last]+self.firstname[index_first]
    def show_phone_number(self):
        print self.get_phone_number()

#身份证号生成
    def get_ID(self):

        #区号

        section_code="411325"

        #生日

        year=random.randint(1950,2000)
        month=random.randint(1,12)


        #闰年共有366天（1-12月分别为31天，29天，31天，30天，31天，30天，31天，31天，30天，31天，30天，31天）
        #公历中 平年2月比闰年少一天

        if month in [4,6,9,11]:
            day=random.randint(1,30)
        elif month ==2:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):  # 闰年
                day=random.randint(1,29)
            else:
                day=random.randint(1,28)
        else:
            day=random.randint(1,31)

        if month < 10:
            month='0'+str(month)
        else:
            month=str(month)

        if day < 10:
            day='0'+str(day)
        else:
            day=str(day)

        birth_code=str(year)+month+day

        #顺序号
        seq_code=random.randint(100,150) #简化处理
        seq_code=str(seq_code)

        #校验号
        id=section_code+birth_code+seq_code
        sum=0
        for i in range(0,len(id)):
            sum+=int(id[i])*self.weight[i]
        verifycode_index=str(sum % 11)

        verify_code=self.id_verifycode[verifycode_index]

        id=id+verify_code
        return id

#银行卡号生成
    def get_BANKCARDID(self):

        #发行卡标识代码
        #建设银行
        issure_code="621700"

        #自定义位
        self_code="".join(random.choice("0123456789") for i in range(12))
        #校验位
        bankid=issure_code+self_code

        # bankid="621700017000772247"
        i=len(bankid)-1
        sum_even=0
        sum_odd=0
        sum=0
        while i>0:
             s_even=2*int(bankid[i])
             sum_even=s_even % 10+s_even / 10
             sum=sum+sum_even+int(bankid[i-1])
             # print sum_even
             # print bankid[i-1]
             i=i-2
        # print sum_even
        # print sum
        if sum>99:
            verify_code=sum %100 % 10
        else:
            verify_code=sum %10
        if verify_code==0:
            verify_code=0
        else:
            verify_code=10-verify_code

        bankcard_id=bankid+str(verify_code)

        return bankcard_id

# 继承BasePage类
class OpenAccountAction(BasePage):
    # 定位器，通过元素属性定位元素对象
    openaccountlink_loc = (By.LINK_TEXT, '去开户')

    #开户四要素
    realname_loc=(By.ID,'realName')
    idcard_loc=(By.ID,'IDCard')
    bankcard_loc=(By.ID,'bankCard')
    bankMobile_loc=(By.ID,'bankMobile')

    accountinfosubmit_loc=(By.LINK_TEXT,'下一步')

    #上传身份证
    # uploadimgfront_loc=(By.CSS_SELECTOR,'.idFront')
    # uploadimgfront_loc = (By.CSS_SELECTOR, 'div[class="upload-wrap"]>div:nth-of-type(1)')
    uploadimgfront_loc = (By.CSS_SELECTOR, 'div[class="front"]>div:nth-of-type(4)')

    uploadimgback_loc = (By.CSS_SELECTOR, 'div[class="back"]>div:nth-of-type(4)')


    open_submit_loc=(By.LINK_TEXT,'提交开户')
    #上行短信验证码按钮
    SmsVerifybtn_loc=(By.ID,'sendSmsVerify')
    Smscodetext_loc=(By.ID,'smsCode')

    Smspassword_loc = (By.ID, 'password')
    Smsconfirmpassword_loc=(By.ID,'confirmPassword')

    #短信验证码弹窗
    Smsalert_loc=(By.LINK_TEXT,'我知道了')

    #同意协议并注册
    agreeandsubmit_loc=(By.ID,'nextButton')

    #开户结果
    result_fail_id=(By.ID,'applyFail')
    result_success_id=(By.ID,'applySuccess')
    result_text="开户申请提交成功"

    TEL=""
    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        # self.base_url = base_url

    def getaccountinfo(self):
        person = Person()
        self.realname = person.return_new_name()
        self.identify=cf.get('webauto','open_account_ID')
        self.bankcardid=cf.get('webauto','open_account_BANKNo')
        if not self.identify and not self.bankcardid:

            self.identify = person.get_ID()
            self.bankcardid = person.get_BANKCARDID()
        elif not self.identify:
            self.identify = person.get_ID()
        elif not self.bankcardid:
            self.bankcardid = person.get_BANKCARDID()
        else:
            pass


        #生成身份证图片
        comm.IDCreate(self.realname,self.identify)


    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    # 开户页面打开
    def openaccount_click(self):
        self.find_element(*self.openaccountlink_loc).click()

    #四要素填写
    def input_realname(self):


        self.find_element(*self.realname_loc).send_keys(self.realname)

    def input_id(self):

        txt=cf.get('webauto', 'open_account_ID')
        if txt:
            identify=txt
        else:
            identify=self.identify
        self.find_element(*self.idcard_loc).send_keys(identify)

    def input_bankid(self):
        txt = cf.get('webauto', 'open_account_BANKNo')
        if txt:
            bankcardid=txt
        else:
            bankcardid=self.bankcardid
        self.find_element(*self.bankcard_loc).send_keys(bankcardid)


    def input_mobile(self):

        mobile=cf.get('webauto','open_account_bankMobile')
        self.find_element(*self.bankMobile_loc).send_keys(mobile)


    def submit_click(self):
        self.find_element(*self.accountinfosubmit_loc).click()

    def accountinfo_submit(self):
        self.input_realname()
        self.input_id()
        self.input_bankid()
        self.input_mobile()
        # self.accountinfo_submit()
        self.submit_click()



    def uploadimg(self):
        time.sleep(2)
        self.find_element(*self.uploadimgfront_loc).click()

        #上传肖像面
        posfront='D:\\IDfront.png'
        comm.winUpload(posfront)
        time.sleep(5)

        #上传国徽面
        self.find_element(*self.uploadimgback_loc).click()
        posback = 'D:\\IDback.png'
        comm.winUpload(posback)
        time.sleep(5)

    def submit_openaccout(self):

        ele=self.find_element(*self.open_submit_loc)
        ele.click()

        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                break
        # driver.switch_to.window(handles[0])


    def input_smsverifycode(self):
        time.sleep(1)
        self.find_element(*self.SmsVerifybtn_loc).click()
        time.sleep(1)
        self.smsalert_click()
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



