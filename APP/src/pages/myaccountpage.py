# coding=utf-8

from portalpage import PortalPage


class MyAccountPage(PortalPage):


    def __init__(self,myaccountloc):

        super(MyAccountPage,self).__init__()
        #进入相应模块

        self.click_navigationbtn(myaccountloc)
        pass




