# coding=utf-8

import os
import sys
import time

from selenium.webdriver.common.by import By


from myaccountpage import MyAccountPageAction

class InvestPageAction(MyAccountPageAction):
    # 定位器，通过元素属性定位元素对象
    myaccountlink_loc = (By.LINK_TEXT, '我的账户')

    #项目详情页，投资限额
    limitinvestamt_loc=(By.CLASS_NAME,'limitInvestAmt')
    balanceamt_loc=(By.CLASS_NAME,'balance')

    quickinvestbtn_loc=(By.LINK_TEXT,'立即投资')

    investamttext_loc=(By.CSS_SELECTOR,'input[name="amount"]')

    riskpop_loc=(By.ID,'projectInvest3')
    agreeinvest_loc=(By.ID,'agreeInvest3')
    confirmInvest_loc=(By.LINK_TEXT,'确认投资')




    #交易密码
    password=(By.ID,'password')
    #懒猫页面确认支付按钮
    agreeprotocol_loc=(By.ID,'nextButton')


    #投资项目选择逻辑js
    invest_js1 = ("projectarray=document.querySelector('.projectList').getElementsByTagName('a');"
          "showbtn=document.querySelector('.showMore');"
          "var num=Math.ceil(arguments[0]/10);var i=0;"
          "while (i<num){showbtn.querySelector('p[style=\"display: block;\"]').click();i++};")
    invest_js2=(
          "var newproject=new Array();"
          "for(var j=0;j<projectarray.length;j++){"
          "var invest=projectarray[j].querySelector('div.INVESTING');"
          "var invest_text=invest.innerText;"
          "if(invest_text=='立即投资'){var invest_remainamount=invest.nextSibling.innerText;"
          "var remainamount=Number(invest_remainamount.match(/\d+/g));"
          "if(remainamount>=arguments[0]){newproject.push(j)}}};"
          "var newproject_length=newproject.length;var rand=Math.floor(Math.random()*newproject_length);"
          "projectarray[rand].click();return newproject")


    #当前页面相对地址
    invest_path="/project/list"


    #指定投资项目范围，选中一个，参数0：从多少个项目中选，参数1：预投资金额
    def select_investproject(self,range,investamt):

        self.driver.execute_script(self.invest_js1,range)
        time.sleep(10)
        self.driver.execute_script(self.invest_js2,investamt)

        #

        pass

    #项目详情页信息,返回起投金额和上限
    def get_limitinvestamt(self):
        limitamt=self.find_element(*self.limitinvestamt_loc).text

        balanceamt=self.find_element(*self.balanceamt_loc).text

        amttext=limitamt.split("，")

        #unicode 字符 中文字符也是占一位
        min_investamt=amttext[0][:-3]
        max_investamt=amttext[1][:-1][2:]
        # print amttext
        return [int(min_investamt),int(max_investamt),int(balanceamt)]
        pass

    def click_quickinvestbtn(self):

        #用户CA弹窗处理
        time.sleep(2)
        if self.is_alert_exist():
            pass

        self.find_element(*self.quickinvestbtn_loc).click()


    #输入投资金额
    def input_investamt(self,amt):
        # self.click_quickinvestbtn()
        if self.is_element_exist(self.riskpop_loc):
            self.find_element(*self.agreeinvest_loc).click()
            self.find_element(*self.confirmInvest_loc).click()
        ele=self.find_element(*self.investamttext_loc)
        ele.clear()
        ele.send_keys(amt)

    # def is_riskpop_exist(self):
    #     if
    #
    #         return True
    #     else:
    #         return False

    #同意上行协议并支付
    def input_TradingPassword(self,password):
        self.find_element(*self.password).send_keys(password)
        self.find_element(*self.agreeprotocol_loc).click()


    #是否在我的账户-充值页(默认转账充值页)
    def is_on_investpage(self):
        pathnamestr="return "+"document.location.pathname"
        pathname=self.driver.execute_script(pathnamestr)

        if pathname ==self.invest_path:
            return True
        else:
            return False













