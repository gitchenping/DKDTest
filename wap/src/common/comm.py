# coding=utf-8

from selenium.webdriver.common.by import By
from basepage import BasePage
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import win32gui
import win32con

import pytesseract

import random
import time
import ConfigParser
import pymysql
import os
import sys


wappath=os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
toolpath=wappath+"\\tools\\"

config_path=wappath+"\\config\\config.ini"
cf=ConfigParser.ConfigParser()
cf.read(config_path)

class DB():
    def __init__(self):
        self.db_host=cf.get('wapauto','db_host')
        self.db_port=cf.get('wapauto','db_port')
        self.db_name=cf.get('wapauto','db_name')
        self.db_password=cf.get('wapauto','db_password')
        self.db_db=cf.get('wapauto','db_db')

    def dbconn(self):
        conn = pymysql.connect(self.db_host,self.db_name,self.db_password,self.db_db)
        return conn
    def dbsearch(self,sql):
        cursor=self.dbconn().cursor()
        cursor.execute(sql)
        resList = cursor.fetchall()

        # 查询完毕后必须关闭连接
        cursor.close()
        self.dbconn().close()
        return resList

#构造个人信息：如手机号，身份证号等
class PersonInfo():

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
    def get_Phonenumber(self):
        index=random.randint(0,len(self.prefix_phone)-1)
        return self.prefix_phone[index] + "".join(random.choice("0123456789") for i in range(8))

    #姓名
    def get_Newname(self):
        index_last = random.randint(0, len(self.lastname) - 1)
        index_first=random.randint(0, len(self.firstname) - 1)
        return self.lastname[index_last]+self.firstname[index_first]

    def show_phone_number(self):
        print self.get_Phonenumber()

    #身份证号生成
    def get_NEWID(self):

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


#生成一个身份证图片
def get_IDIMG(name,id):
    person = PersonInfo()

    NAME = name
    # info to show
    ID = id

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
    idfont=toolpath+"hwxh_font.ttf"
    font_id = ImageFont.truetype(idfont, 29)
    # for name
    namefont=toolpath+"simhei.ttf"
    font_name = ImageFont.truetype(namefont, 25)
    # for address sex nation
    font_asn = ImageFont.truetype(namefont, 20)

    # 打开底板图片和头像
    imageFile = toolpath+"base.png"
    imagephoto = toolpath+"head.png"
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
    # im.show()
    # 另存为
    portraiture=toolpath+"portraiture.png"
    im.save(portraiture)
    pass


#截图-验证码，并识别
#imgfilepath:图片全路径；imgsize:图片验证码相对图片的位置，元祖形式
def imgverifycode_recongnise(srcimgfilepath,dstimgfilepath,imgcodesize):

    i = Image.open(srcimgfilepath)  # 打开截图
    result = i.crop(imgcodesize)  # 使用Image的crop函数，从截图中再次截取我们需要的区域

    img = result.resize((395, 225), Image.ANTIALIAS)
    img.save(dstimgfilepath)

    ii = Image.open(dstimgfilepath)

    text = pytesseract.image_to_string(ii, 'eng')

    return text


# 如果，验证码错误，重新刷新验证码，再次输入，验证次数10次

#上传文件，参数为文件全路径
def winUpload(filepos):
    time.sleep(3)
    dialog = win32gui.FindWindow(0, u'打开')  # 找到windows对话框参数是（className，title）
    # print dialog
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    # 上面3句依次找对象，直到找出输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮
    # 跟上面示例的代码是一样的，只是这里传入的参数不同，如果愿意可以写一个上传函数把上传功能封装起来
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filepos)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    pass

