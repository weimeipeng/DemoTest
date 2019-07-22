#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import json

if __name__ == "__main__":
    print("python json标准库解析实例")

    # python对象转json对象
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

    json_data = json.dumps(data)

    # 打印出来看下效果
    print("转化前")
    print(type(data))
    print(data)
    print("-" * 40)
    print("转化后")
    print(type(json_data))
    print(json_data)

    # 将json对象转化成python对象
    print()
    print("将json对象转化成python对象")
    python_data = json.loads(json_data)
    print(type(python_data))
    print(python_data)

    # 请仔细查看结果参照《python原始类型与json类型的转化对照表》对比转化前后的变化