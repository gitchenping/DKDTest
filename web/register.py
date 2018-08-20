# coding=utf-8
"""页面基本操作方法：如open，input_username，input_password，click_submit"""
from selenium.webdriver.common.by import By
from basepage import BasePage
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ConfigParser

import random
import time
import sys

# from pytesseract import image_to_string
import pytesseract

cf=ConfigParser.ConfigParser()
cf.read('D:\\NewPythonWorkplace\\config.ini')

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
        issure_code="622848"

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
class RegisterPageAction(BasePage):
    # 定位器，通过元素属性定位元素对象
    accountlink_loc = (By.LINK_TEXT, '注册')
    username_loc=(By.NAME,'registerName')
    password_loc = (By.NAME, 'registerPwd')
    imgcodetext_loc = (By.NAME, 'imgCode')
    msgcode_loc = (By.NAME, "msgCode")
    imagecode=(By.CLASS_NAME,"kaptcha")
    iconrefresh_loc=(By.CLASS_NAME,"icon-refresh")
    verifycode_loc=(By.CLASS_NAME,"verifyCode")
    submit_loc=(By.LINK_TEXT,"立即注册")

    TEL = ""
    IMG_VERIFY_FAIL=0
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    #ACCOUNT
    def click_account(self):
        self.find_element(*self.accountlink_loc).click()

#截图-验证码，并识别
    def screen_img_shot(self):
        n=0
        for n in range(0,10):
             #截图，当前窗口
            self.driver.save_screenshot("D:\\all.png")
            imageelemnt=self.driver.find_element(*self.imagecode)
            location=imageelemnt.location   # 获取验证码图片x,y轴坐标
            size=imageelemnt.size   # 获取验证码的长宽

            rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
            i = Image.open("D:\\all.png")  # 打开截图
            result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
            img = result.resize((395, 225), Image.ANTIALIAS)
            img.save('D:\\result.png')
            ii=Image.open('D:\\result.png')

            text = pytesseract.image_to_string(ii, 'eng')


        #  如果，验证码错误，重新刷新验证码，再次输入，验证次数10次
        # 点击获取短信验证码（此步校验图片验证码是否识别正确）
            time.sleep(1)
        # 长度判断，非5个字符，肯定不对
            if len(text) < 5 or len(text) >= 6:
                # self.driver.find_element(*self.imgrefresh_loc).click()

                 self.driver.execute_script('document.getElementsByClassName("icon-refresh")[0].click()')

                 continue
            else:
                #     print text
                time.sleep(1)
                self.driver.find_element(*self.imgcodetext_loc).send_keys(text)

                self.driver.find_element(*self.verifycode_loc).click()
                time.sleep(2)
                # 如果有提示，说明验证码错误
                js1 = 'document.getElementsByClassName("imgTip")[0].innerText'
                imgtip = self.driver.execute_script('return ' + js1)

                if imgtip!="":
                    self.driver.find_element(*self.imgcodetext_loc).clear()
                    self.driver.execute_script('document.getElementsByClassName("icon-refresh")[0].click()')
                else:
                    # 查询数据库验证码
                    self.driver.find_element(*self.msgcode_loc).send_keys("1234")
                    break
        #中止识别
        if n<=10:
            pass
        else:
            self.IMG_VERIFY_FAIL=1



# 输入用户名：调用send_keys对象，输入手机号
    def input_username(self):
        #        self.find_element(*self.username_loc).clear()
        # 输入手机号
        if not cf.get("webauto", "register_username"):
            tel = Person().get_phone_number()
        else:
            tel = cf.get("webauto", "register_username")
        self.TEL = tel
        self.find_element(*self.username_loc).send_keys(tel)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self):
        #        self.find_element(*self.password_loc).clear()
        password = cf.get("webauto", "register_password")
        self.find_element(*self.password_loc).send_keys(password)
     # 点击登录：调用send_keys对象，点击登录

    def click_submit(self):
        if self.IMG_VERIFY_FAIL:
            sys.exit(1)
        else:
            self.find_element(*self.submit_loc).click()
    #
    #     # 登录成功页面中的用户ID查找
    #
    # def show_userid(self):
    #     return self.find_element(*self.userid_loc).text


def meger_ID():
    person = Person()
    person.show_phone_number()

    # info to show
    ID = person.get_ID()
    NAME = person.return_new_name()
    print ID
    print person.get_BANKCARDID()
    # 提取出生日期
    birth_year = ID[6:10]
    birth_month = ID[10:12]
    birth_day = ID[12:14]

    # 判断性别
    if int(ID[16]) % 2 == 0:
        sex = u"女"
    else:
        sex = u"男"
    # 民族
    nation = u"汉"

    # 设置所使用的字体
    '''“姓名”、“性别”、“民族”、“出生年月日”、“住址”、“公民身份号码”为6号黑体字，用蓝色油墨印刷;登记项目中的姓名项用5号黑体字印刷;其他项目则用小5号黑体字印刷;
    身份证号码字体   OCR-B 10 BT   文字 华文细黑
    '''
    # font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 26)
    # for ID
    font_id = ImageFont.truetype("F:\\test_tool\\hwxh_font.ttf", 29)
    # for name
    font_name = ImageFont.truetype("F:\\test_tool\\simhei.ttf", 25)
    # for address sex nation
    font_asn = ImageFont.truetype("F:\\test_tool\\simhei.ttf", 20)

    # 打开底板图片和头像
    imageFile = "F:\\test_tool\\base.png"
    imagephoto = "F:\\test_tool\\6.png"
    im = Image.open(imageFile)
    im1 = Image.open(imagephoto)
    # 对头像增加alpha通道
    r, g, b, a = im1.convert('RGBA').split()
    im1.putalpha(a)
    # im1.resize((500,400),Image.ANTIALIAS)
    # print dir(im)
    # 像素值
    px = im.size
    x = px[0]
    y = px[1]
    x_offset = 0.32 * x
    y_offset = 0.83 * y
    # print px[0]
    im.paste(im1, (330, 40), mask=a)

    # 画图
    draw = ImageDraw.Draw(im)
    # 设置文字位置/内容/颜色/字体
    draw.text((90, 45), NAME, (0, 0, 0), font=font_name)
    draw.text((90, 125), birth_year, (0, 0, 0), font_asn)
    draw.text((175, 125), birth_month, (0, 0, 0), font_asn)
    draw.text((220, 125), birth_day, (0, 0, 0), font_asn)
    draw.text((100, 90), sex, (0, 0, 0), font_asn)
    draw.text((210, 90), nation, (0, 0, 0), font_asn)
    draw.text((x_offset, y_offset), ID, (0, 0, 0), font=font_id)
    # 显示
    im.show()
    # 另存为
    im.save("D:\\target.png")
    pass






