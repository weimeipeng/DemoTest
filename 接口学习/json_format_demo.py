#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import json

if __name__ == "__main__":
    print("python json串格式化实例")

    data = [ { 'c' : 3, 'a' : 1, 'b' : 2, 'd' : 4, 'e' : 5 } ]

    json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    
    # 打印格式化的json串
    print(json_data)