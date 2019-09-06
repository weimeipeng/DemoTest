#5-14 PageObject实践(3)—Login模块封装
#封装登录操作 / 业务逻辑进行封装：

#导入基础模块：
import sys
sys.path.append("C:/Users/tyl/Desktop/Unit5")
import logging
from page_object.common_fun import Common #导入公共类：
from page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By

#定义一个新的"登录"类：
#存储在一个变量里面：
class LoginView(Common): #继承了common；
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    #封装"登录"方法：
    def login_action(self,username,password):
        #检测升级弹窗&跳过：
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('=====login=====')
        logging.info('input username:%s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn ).click()
        logging.info('login finished')

if __name__=='__main__':
    #common又继承了baseView：
    driver=appium_desired() #必须driver初始化；
    l=LoginView(driver) #定义好的初始化；
    l.login_action('测试666','jzy123456')
