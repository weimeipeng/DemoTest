#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import yaml

if __name__ == "__main__":
    print("python yaml基本示例")

    document = """
    公众号: 开源优测
    基本信息:
        创建人: 苦叶子
        id: DeepTest
    """

    # 将yaml格式内容 转换成 dict类型
    load = yaml.load(document)
    print(type(load))
    print(load)

    print("---" * 25)
    # 将python对象转换成为yaml格式文档
    output = yaml.dump(load)
    print(type(output))
    print(output)
