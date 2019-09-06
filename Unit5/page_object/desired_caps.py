#5-12 PageObject实践(1)—Capability封装
#封装了appium的APP启动的模块：

#导入基础模块：
import yaml
import logging
import logging.config
from os import path
from appium import webdriver

CON_LOG='../Log/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

#单独定义一个方法：
def appium_desired():
    #读取yaml数据表：
    stream=open('../yaml/capability.yaml','r')
    data = yaml.load(stream,Loader=yaml.FullLoader)

    # 获取数据：
    desired_caps = {}  # 定义存储信息：
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['noReset'] = data['noReset']

    #输入中文的话，需要定义这2个参数：
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    #打印日志，启动APP：
    logging.info('start run app......')
    driver = webdriver.Remote('http://'+ str(data['ip'])+ ':'+ str(data['port']) + '/wd/hub',desired_caps)

    #设置隐式等待：
    driver.implicitly_wait(8)
    return driver

if __name__=='__main__':
    appium_desired()



