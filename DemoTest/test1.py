from selenium import webdriver

if __name__ == '__main__':

    # wdriver.close() #关闭当前窗口，如果当前只打开一个窗口，该命令将关闭浏览器
    # wdriver.quit() #关闭所有窗口，并退出浏览器
    # wdriver.refresh()#刷新当前页面，等价于 浏览器的 F5 刷新


    wdriver = webdriver.Firefox()  # 创建 用于操作 火狐浏览器的 webdriver 对象
    wdriver.get("http://www.baidu.com")  # 调用对象的 get() 方法，启动浏览器 打开制定页面

    # wdriver.find_element_by_id("kw").send_keys("自动化测试")
    #在页面中查找 ID 为 “kw” 的元素，并在该元素中输入 ：自动化测试
    # title = wdriver.title  #获取当前页面的title 内容

    # wdriver.page_source #获取当前页面渲染后的源代码
    # wdriver.current_url #获取当前页面URL 地址
    # print(wdriver.page_source)
    # print(wdriver.current_url)

    wdriver.find_element_by_link_text("新闻").click()
    # 在页面中查找 文本 为 “新闻” 的链接标签，并执行点击操作
    wdriver.quit()