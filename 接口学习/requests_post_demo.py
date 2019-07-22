#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import requests

if __name__ == "__main__":
    print("requests post示例")

    # 目标url
    url = "http://httpbin.org/post"

    # 请求头headers
    headers = {"custom-header": "mypost"}

    # 要post的数据
    data = {"data_1": "deeptest", "data_2": "testingunion.com"}

    # 发送post请求
    r = requests.post(url, data=data, headers=headers)

    # 输出结果
    print(r.text)
