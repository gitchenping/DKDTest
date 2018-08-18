#coding=utf-8
from APP.src.common.uihelper import Driver
from appium.webdriver.common.mobileby import MobileBy
import time
import os
from appium.webdriver.common.touch_action import TouchAction

# driver = Driver().getDriver()

from APP.src.common import uihelper
import subprocess

def sh(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print p.stdout.read().decode('gbk')

def push_id(srcpath, dstpath="/sdcard/myfile/portraiture.png"):
    uihelper.cleardevfile(dstpath)
    uihelper.pushfile(srcpath)  # 传给安卓设备
    # adb_cmd = "adb shell rm " + dstpath
    #
    # os.system(adb_cmd)

wappath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
toolpath=wappath+"\\APP\\tools\\"

headimgpath=toolpath+"portraiture.png"
# print headimgpath

push_id(headimgpath)

# adb_cmd = "adb shell rm "+headimgpath
# sh(adb_cmd)

# os.system('D:\\工作软件\\win-test\\sdk\\sdk\\platform-tools\\adb')
# sh('adb')
