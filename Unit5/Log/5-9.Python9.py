#5-9 Logging模块综合实践
#测试场景：测试考研帮APP的脚本增加log采集的功能，设置指定的日志格式输出，并将日志保存到指定文件；

#导入模块：
from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging

file=open('../yaml/capability.yaml','r')
data=yaml.load(file,Loader=yaml.FullLoader)

logging.basicConfig(level=logging.INFO,filename='runlog.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

#获取数据：
desired_caps={} #定义存储信息：
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']

logging.info('start app......')
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
