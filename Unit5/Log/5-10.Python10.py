#5-10 Logging配置文件管理：
from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException

import logging
import logging.config

stream=open('../yaml/capability.yaml','r')
data=yaml.load(stream,Loader=yaml.FullLoader)

CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

#获取数据：
desired_caps={} #定义存储信息：
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']

#logging.info('start app......')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+ '/wd/hub',desired_caps)

def check_cancelBtn():
    logging.info('check cancelBtn！')

    try:
        cancelBtn=driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    logging.info('check skipBtn！')

    try:
        skipBtn=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info('no skipBtn')
    else:
        skipBtn.click()

#最后调用2个方法(1.取消升级；2."跳过")：
check_cancelBtn()
check_skipBtn()
