#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import json

if __name__ == "__main__":
    print("python 读取json内容文件转化python对象实例")

    fp = open('json_data.json', 'r')
 
    json_data = json.load(fp)
    print(type(json_data))
    print(json_data)

    fp.close()