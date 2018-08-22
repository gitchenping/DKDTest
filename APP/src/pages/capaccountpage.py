# coding=utf-8

from myaccountpage import MyAccountPage
from appium.webdriver.common.mobileby import MobileBy

from APP.config.By import BankList_LOC,CAPACCOUNT_LOC,AccountInfo_LOC,LMOpen_LOC

from APP.src.common import uihelper
from appium.webdriver.common.touch_action import TouchAction
import os


class CapAccountPage(MyAccountPage):

    # loc=(By.CLASS_NAME,'android.widget.LinearLayout')


    def __init__(self,myaccountloc,capaccountloc):

        super(CapAccountPage,self).__init__(myaccountloc)
        #进入相应模块

        # self.click_navigationbtn(myaccountloc)
        self.comfindElement(capaccountloc).click()
        pass

    #
    def get_capaccount_info(self):
        '''资金账户信息'''
        pass

    def fill_capaccount_info(self,realname,id,bankcard,tel='18811345809'):
        '''填写开户信息'''

        self.comfindElement(CAPACCOUNT_LOC['RealName']).send_keys(realname)
        self.comfindElement(CAPACCOUNT_LOC['ID']).send_keys(id)
        self.comfindElement(CAPACCOUNT_LOC['BankCard']).send_keys(bankcard)

        #选择banklist
        self.comfindElement(CAPACCOUNT_LOC['BankList']).click()

        bancard_verifycode=bankcard[0:6]

        #中行
        boc_list=['621660','621661','621662','621663','621665','621667']
        #建行
        ccb_list=['621700','436742','436745','622280']
        #工行
        icbc_list=['622202','622208']
        #农业
        abc_list=['622848']
        #交行
        bcm_list=['622260','622262']


        nav_pos=""
        if bancard_verifycode in boc_list:
            nav_pos = BankList_LOC['BOC']
        elif bancard_verifycode in ccb_list:
            nav_pos=BankList_LOC['CCB']
        elif bancard_verifycode in icbc_list:
            nav_pos=BankList_LOC['ICBC']
        elif bancard_verifycode in abc_list:
            nav_pos=BankList_LOC['ABC']
        elif bancard_verifycode in bcm_list:
            nav_pos=BankList_LOC['BCM']
        else:
            nav_pos=BankList_LOC['BOC']
            pass

        nav = (MobileBy.ANDROID_UIAUTOMATOR, nav_pos)

        self.findElement(nav).click()



        #隐藏软键盘
        # self.driver.hide_keyboard()
        self.comfindElement(CAPACCOUNT_LOC['Tel']).send_keys(tel)

        self.comfindElement(CAPACCOUNT_LOC['NextStep']).click()


        pass

    def init_accountinfo(self,realname=None, id=None, bankcard=None, tel=None):


        accountinfo = uihelper.create_mockaccountinfo(realname, id,bankcard, tel)
        # print ['set', name, identify, bankcardid, tel]
        uihelper.get_IDIMG(accountinfo[0], accountinfo[1])

        return accountinfo

    def push_idimg(self,srcpath,dstpath="/sdcard/myfile/portraiture.png"):

        uihelper.cleardevfile(dstpath)
        uihelper.pushfile(srcpath)# 传给安卓设备


    def uploadidshot(self):

        #根据坐标选择照片
        #1、选择照片-肖像照
        self.comfindElement(CAPACCOUNT_LOC['ImgLeft']).click()

        piclist_pos = self.getElementsize(CAPACCOUNT_LOC['PictureList'])
        pic_pos = self.getElementsize(CAPACCOUNT_LOC['Picture'])

        touch = TouchAction(self.driver)
        touch.tap(None, piclist_pos[2]/2, pic_pos[1] + pic_pos[3]/2).perform()


        #2、选择-国徽面
        self.comfindElement(CAPACCOUNT_LOC['ImgRight']).click()

        touch.tap(None, piclist_pos[2]/6*5, pic_pos[1] + pic_pos[3] / 2).perform()

        self.comfindElement(CAPACCOUNT_LOC['OpenAccountBtnSubmit']).click()



        pass

    def fill_lminfo(self,tradepassword):

        adb_cmd = "adb shell monkey  -f /sdcard/myfile/login.txt -v 1"

        os.system(adb_cmd)


        # #获取验证码
        # navcode=LMOpen_LOC['VerifyCodeBtn']
        # navcode_pos=(MobileBy.ACCESSIBILITY_ID,navcode)
        # know=LMOpen_LOC['Know']
        # know_pos=(MobileBy.ACCESSIBILITY_ID,know)
        #
        # # self.findElement(navcode_pos).click()
        # # self.findElement(know_pos).click()
        #
        # #填写短信验证码、交易密码
        # msgcode_tradecode=(MobileBy.CLASS_NAME,LMOpen_LOC['VerifyCodeText'])
        # ele=self.findElements(msgcode_tradecode)
        # print self.driver.context
        # # ele=self.driver.find_elements_by_class_name(LMOpen_LOC['VerifyCodeText'])
        # print ele
        # ele[0].send_keys('1234')
        # ele[1].send_keys(tradepassword)
        # ele[2].send_keys(tradepassword)



        #同意协议并注册
        # register=LMOpen_LOC['RegisterBtn']
        # register_loc=(MobileBy.ACCESSIBILITY_ID,register)
        # self.findElement(register_loc).click()

        pass


    def get_accountinfo(self):

        name=self.get_eletext(AccountInfo_LOC['Name'])
        id=self.get_eletext(AccountInfo_LOC['Id'])
        accountno=self.get_eletext(AccountInfo_LOC['Account'])
        bankname=self.get_eletext(AccountInfo_LOC['Account'])
        banklocation=self.get_eletext(AccountInfo_LOC['BankLocation'])

        return [name,id,accountno,bankname,banklocation]
        pass

    def check_accountinfo(self,name,id):

        accountinfo=self.get_accountinfo()

        namestr=accountinfo[0].strip('*')
        idstr_one=accountinfo[1][0:6]
        idstr_two=accountinfo[1][10:13]

        return namestr in name and idstr_one in id and idstr_two in id

        pass

    def back_navpage(self):

        self.keyaction(4)

        self.keyaction(4)






