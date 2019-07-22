#-*- coding:utf-8 -*-


__author__ = "苦叶子"

from urllib.parse import urlparse


if __name__ == "__main__":
    print("urllib url切割实例")

    url = "http://username:password@www.baidu.com:80/q=开源优测"

    result = urlparse(url)

    print("看下切割后的整体结果: ")
    print(result)

    print("协议: ", result.scheme)
    print("连接字符串：", result.netloc)
    print("hostname:", result.hostname)
    print("端口号：", result.port)
    print("uri资源：", result.path)
    print("用户名：", result.username)
    print("密码：", result.password)
