#5-13 PageObject实践(2)—公共类封装

#封装基类：
#定义"初始化"类：
class BaseView(object):
    #driver的初始化：
    #初始化把driver传入：
    def __init__(self,driver):
        self.driver=driver #存入当前对象；

    #"元素定位"方法的封装：
    def find_element(self,*loc): # *loc代表可变参数；
        return self.driver.find_element(*loc)
