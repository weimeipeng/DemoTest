#-*- coding:utf-8 -*-


__author__ = "苦叶子"

import urllib.request

if __name__ == "__main__":
    print("读取www.python.org首页的html源码")

    response = urllib.request.urlopen("http://www.python.org")

    print("打印下结果")

    print(response.read())

    