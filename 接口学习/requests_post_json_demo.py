#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import requests

if __name__ == "__main__":
    print("requests post json数据示例")

    # 目标服务url
    url = "http://jsonplaceholder.typicode.com/posts"

    # 自定义头
    headers = {
        "custom-post": "my-post",
        "custom-header": "my-json-header"
        }

    # 要post的数据
    json_data = {
        "title": "deeptest",
        "body": "开源优测",
        "userId": "1"
        }

    # post json格式的数据
    r = requests.post(url, json=json_data, headers=headers)

    # 打印下返回结果
    print(r.text)
    