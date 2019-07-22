#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import requests

if __name__ == "__main__":
    r = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx5c4e7f7d1be0d4b1&secret=bda208328bf54332fd989f9a274fc7e0 ")

    print(r.text)
