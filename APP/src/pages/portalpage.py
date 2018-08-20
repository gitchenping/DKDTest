# coding=utf-8

from appium.webdriver.common.mobileby import MobileBy

from APP.src.common.basepage import BasePage


class PortalPage(BasePage):

    # loc=(By.CLASS_NAME,'android.widget.LinearLayout')

    def get_navgatorelement(self,pos):

            #mock
            # elements = self.mock_comfindElement(pos)

            #online
            # elements=self.comfindElement(pos)

            # elements=
           pass

    def click_navigationbtn(self,nav_pos):

        #元祖

        nav=(MobileBy.ANDROID_UIAUTOMATOR,nav_pos)

        self.findElement(nav).click()
