#5-15 PageObject实践(4)—unittest用例封装

#导入基础模块：
from Unit5.page_object.desired_caps import appium_desired
import unittest
import logging
from time import sleep

#定义一个新的类：
class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp=====')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('=====tearDown=====')
        sleep(5)
        self.driver.close_app()
