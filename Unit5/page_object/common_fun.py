#5-13 PageObject实践(2)—公共类封装
#封装通用公共类：

#导入基础模块：
import sys
sys.path.append("C:/Users/tyl/Desktop/Unit5")
from page_object.baseView import BaseView
from page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        logging.info("=====check_cancelBtn=====")

        try:
            element=self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('update element is not found!')
        else:
            logging.info('click cancelBtn')
            element.click()

    def check_skipBtn(self):
        logging.info('=====check_skipBtn=====')
        try:
            element=self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skipBtn element is not found!')
        else:
            logging.info('click skipBtn')
            element.click()

if __name__=='__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()


