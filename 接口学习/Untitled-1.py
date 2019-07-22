from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    wd = webdriver.Firefox()
    wd.get("http://www.baidu.com")

    wd.find_element_by_id("kw").send_keys("自动化测试")
    sleep(5)
    wd.quit()