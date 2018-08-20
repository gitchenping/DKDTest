#-*- coding:utf-8 -*-
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ConfigParser

import random
import os


#read config

cf=ConfigParser.ConfigParser()

# file_path=os.getcwd()

cf.read('D:\\pycharm worker\\config.ini')

#取ID
ID=cf.get('test','ID')



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
    def return_new_phone_number(self):
        index=random.randint(0,len(self.prefix_phone)-1)
        return self.prefix_phone[index] + "".join(random.choice("0123456789") for i in range(8))
    def return_new_name(self):
        index_last = random.randint(0, len(self.lastname) - 1)
        index_first=random.randint(0, len(self.firstname) - 1)
        return self.lastname[index_last]+self.firstname[index_first]
    def show_phone_number(self):
        print self.return_new_phone_number()

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
        idsum=0
        for i in range(0,len(id)):
            idsum+=int(id[i])*self.weight[i]
        verifycode_key=str(idsum % 11)

        verify_code=self.id_verifycode[verifycode_key]

        id=id+verify_code
        return id

    def get_BANKCARDID(self):

        #发行卡标识代码
        issure_code=cf.get('test', 'bank_issure_code')
        if issure_code:
            pass
        else:
            #中国建设
            issure_code = "621700"

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


def new_id_code():
    pass
def new_phone_number():

    pass

def addTransparency(img, factor = 0.7 ):
    img = img.convert('RGBA')
    img_blender = Image.new('RGBA', img.size, (0,0,0,0))
    img = Image.blend(img_blender, img, factor)
    return img

# from PIL import Image
# im=Image.open("F:\\test_tool\\66.png")
# im=im.convert('RGBA')
# datas=im.getdata()
# newData=list()
# for item in datas:
#         if item[0] >10 and item[1] > 10 and item[2] > 10:
#             newData.append(( item[0], item[1], item[2], 0))
#         else:
#             newData.append(item)
# im.putdata(newData)

person=Person()
person.show_phone_number()

#info to show
if not ID:
    ID= person.get_ID()

NAME=person.return_new_name()
# NAME=u"陈平"
print ID

#BANK_ID
BANK_ID=person.get_BANKCARDID()
print BANK_ID

#提取出生日期
birth_year=ID[6:10]
birth_month=ID[10:12]
birth_day=ID[12:14]

#判断性别
if int(ID[16])%2==0:
    sex=u"女"
else:
    sex=u"男"
#民族
nation=u"汉"

#设置所使用的字体
'''“姓名”、“性别”、“民族”、“出生年月日”、“住址”、“公民身份号码”为6号黑体字，用蓝色油墨印刷;登记项目中的姓名项用5号黑体字印刷;其他项目则用小5号黑体字印刷;
身份证号码字体   OCR-B 10 BT   文字 华文细黑
'''
# font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 26)
#for ID
font_id = ImageFont.truetype("F:\\test_tool\\hwxh_font.ttf", 29)
#for name
font_name = ImageFont.truetype("F:\\test_tool\\simhei.ttf", 25)
#for address sex nation
font_asn=ImageFont.truetype("F:\\test_tool\\simhei.ttf", 20)

#打开底板图片和头像
imageFile = "F:\\test_tool\\base.png"
imagephoto="F:\\test_tool\\6.png"
im= Image.open(imageFile)
im1=Image.open(imagephoto)
#对头像增加alpha通道
r,g,b,a=im1.convert('RGBA').split()
im1.putalpha(a)
# im1.resize((500,400),Image.ANTIALIAS)
# print dir(im)
#像素值
px=im.size
x=px[0]
y=px[1]
x_offset=0.32*x
y_offset=0.83*y
# print px[0]
im.paste(im1,(330,40),mask=a)

#画图
draw = ImageDraw.Draw(im)
#设置文字位置/内容/颜色/字体
draw.text((90,45),NAME,(0,0,0),font=font_name)
draw.text((90,125),birth_year,(0,0,0),font_asn)
draw.text((175,125),birth_month,(0,0,0),font_asn)
draw.text((220,125),birth_day,(0,0,0),font_asn)
draw.text((100,90),sex,(0,0,0),font_asn)
draw.text((210,90),nation,(0,0,0),font_asn)
draw.text((x_offset, y_offset), ID, (0, 0, 0), font=font_id)
#显示
im.show()
#另存为
im.save("D:\\target.png")


def getaccountinfo():
    person = Person()
    realname = person.return_new_name()
    identify = cf.get('wapauto', 'open_account_ID')
    bankcardid = cf.get('wapauto', 'open_account_BANKNo')
    if not identify and not bankcardid:

        identify = person.get_ID()
        bankcardid = person.get_BANKCARDID()
    elif not identify:
        identify = person.get_ID()
    elif not bankcardid:
        bankcardid = person.get_BANKCARDID()
    else:
        pass
    print  identify
    print  bankcardid

# getaccountinfo()