#5-5 Yaml综合实战—Capability配置数据与代码分离
#测试场景：将capability的各项参数值与代码进行分离；
#场景分析：把capability.py里面各项写死的配置信息来抽离出来，存放在一个 yaml 配置文件中；
# 使用对象数据类型来存储数据，然后调用load()方法读取数据，从而实现数据和代码的分离。
#1.参数配置：capability.yaml

#导入yaml模块：
from appium import webdriver
import yaml

#获取数据：
#数据发生了变化，可以直接在yaml文件里面进行修改：
file=open('capability.yaml',encoding='utf-8') #打开yaml文件：
data=yaml.load(file,Loader=yaml.FullLoader) #读取yaml里面的文件：

desired_caps={} #定义存储信息：
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']

#driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+ '/wd/hub',desired_caps)


