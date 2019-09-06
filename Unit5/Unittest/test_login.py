
import sys
sys.path.append("C:/Users/tyl/Desktop/Unit5")
from page_object.loginView import LoginView
from Unittest.Myunit import StartEnd
import unittest
import logging

class TestLogin(StartEnd):

    def test_login_ceshi666(self):
        logging.info('=====test_login_ceshi666=====')
        l=LoginView(self.driver)
        l.login_action('测试666','jzy123456')

    def test_login_ceshi777(self):
        logging.info('=====test_login_ceshi777=====')
        l=LoginView(self.driver)
        l.login_action('测试777','jzy123456')

    def test_login_error(self):
        logging.info('=====test_login_error=====')
        l=LoginView(self.driver)
        l.login_action('6666','2222')

if __name__=='__main__':
    unittest.main()


