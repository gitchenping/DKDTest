#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import sys
import mouse
sys.path.append("e:\\python27\\lib\\site-packages\\win32")
import win32con
import win32api
import win32gui

iedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = iedriver
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver=webdriver.Chrome(iedriver,chrome_options=options)

url="http://www.yuntushuguan.com/firsttransfer.jsp?enc=79a2424ac5f8502497f0fc52f7d794b1bef1365ff2f2b306e0fa70824eb59c7eff8fc0a8914efee67958df89a9cd02aa77e23ed93891e7c5b88467134807b716a1cf9ae140a6e3e3f8d0291b36ed0dc5ca4b141b71933c47fa466d43bed1b10750dad7d0831ab35180c645a64e336dcd22d66c7253bb870d2d44deb2dbf02896a20eb35cb5b667f77a9ca7644e6aef74&unitid=7320"

driver.get(url)
time.sleep(3)
n=0
for i in range(262,263):
    driver.find_element_by_id('pageInput').clear()
    driver.find_element_by_id('pageInput').send_keys(str(i))
    driver.find_element_by_name('input').click()
    time.sleep(1)
    n=n+1
    for m in range(0,10):
        js="return "+"document.getElementsByClassName('readerTip')["+str(n-1)+"].style.display"
        display=driver.execute_script(js)
        if display=="none":
          break
        time.sleep(1)


    # xpath='//*[@ id ="reader"]/div/div['+str(i-100)+']/input'
    # ele=driver.find_element_by_xpath(xpath)
    mouse.mouse_r_click(500, 500)
    # ActionChains(driver).context_click(ele).perform()
    time.sleep(1)
    mouse.key_input("v")
    time.sleep(1)
    dialog = win32gui.FindWindow('#32770', u'另存为')  # 查找对话框
    # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    DUIViewWndClassName=win32gui.FindWindowEx(dialog, 0, 'DUIViewWndClassName', None)
    DirectUIHWND=win32gui.FindWindowEx(DUIViewWndClassName, 0, 'DirectUIHWND', None)
    FloatNotifySink=win32gui.FindWindowEx( DirectUIHWND, 0, 'FloatNotifySink', None)
    ComboBox=win32gui.FindWindowEx(FloatNotifySink, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, str(i))  # 往输入框输入上传文件的绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按确认button
    time.sleep(1)
    # driver.find_element_by_id('nextPage').click()






# for i in range(1,51):
#
#     xpath = '//*[@id="jcopeLightBox"]/div[1]/div[2]/div[1]/img[1]'
#     ele = driver.find_element_by_xpath(xpath)
#     ActionChains(driver).context_click(ele).perform()
#     mouse.key_input("v")
#     time.sleep(2)
#     dialog = win32gui.FindWindow('#32770', u'另存为')  # 查找对话框
#     # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
#     # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
#     DUIViewWndClassName=win32gui.FindWindowEx(dialog, 0, 'DUIViewWndClassName', None)
#     DirectUIHWND=win32gui.FindWindowEx(DUIViewWndClassName, 0, 'DirectUIHWND', None)
#     FloatNotifySink=win32gui.FindWindowEx( DirectUIHWND, 0, 'FloatNotifySink', None)
#     ComboBox=win32gui.FindWindowEx(FloatNotifySink, 0, 'ComboBox', None)
#     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
#     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
#
#     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, str(i))  # 往输入框输入上传文件的绝对地址
#     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按确认button
#     time.sleep(2)
#     driver.find_element_by_id('lbNext').click()
#     time.sleep(1)




