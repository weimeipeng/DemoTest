#-*- coding:utf-8 -*-

__author__ = "苦叶子"


# 导入模块
import requests

if __name__ == "__main__":
    print("开源优测 - requests自定义请求头基本示例")

    url = "http://www.baidu.com"

    # 定义自定义请求头数据
    headers = {
        "user-agent": "www.testingunion.com",
        "custom-head": "DeepTest"
    }

    # 发送带自定义头的请求
    r = requests.get(url, headers=headers)
