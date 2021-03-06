#5-11 PageObject设计模式简介
#重构优化思路：
#1.将一些公共的内容(如：check_updateBtn,check_skipBtn,capability)抽离出来；
#2.元素定位方法和元素属性值与业务代码分离；
#3.登录功能模块封装为一个独立的模块；
#4.使用unittest进行用例综合管理；
#需要优化的地方：1.多账号登录；2.异常登录(错误用户名/密码或为空登录)；3.注册；

#Page Object 是Selenium自动化测试项目开发实践的最佳设计模式之一，通过对界面元素的封装减少多余的代码。
#同时在后期维护中，若元素定位发生了变化，只要调整页面元素封装的代码，提高测试用例的可维护性；
