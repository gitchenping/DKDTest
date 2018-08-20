import os
from selenium import webdriver

# iedriver = "D:\IEDriverServer"
# iedriver="D:\chromedriver\chromedriver.exe"
iedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = iedriver
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
# driver = webdriver.Ie(iedriver)
# driver=webdriver.Chrome(chrome_options=options)
driver=webdriver.Chrome(iedriver,chrome_options=options)