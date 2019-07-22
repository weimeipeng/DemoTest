#-*- coding:utf-8 -*-


__author__ = "苦叶子"


import urllib.parse
import urllib.request


if __name__ == "__main__":
    print("urllib API实例演示说明")

    # 访问百度首页
    response=urllib.request.urlopen('http://www.baidu.com')  

    # 打印下首页是html源码
    # 获取完整的响应内容，便于断言其中的特定值
    html=response.read() 
    print(html)

    # 打印下http header信息
    # 有时候我们需要提前header值来用于下一个请求
    header = response.info()
    print(header)

    # 获取下状态码 http响应的status code
    # 接口测试的一个断言，就是断言状态码
    status_code = response.getcode()
    print(status_code)

    # 打印下本次请求的目标url
    url = response.geturl()
    print(url)