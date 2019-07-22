#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import yaml
import codecs

if __name__ == "__main__":
    print("python yaml基本示例")
    
    fp = codecs.open("yaml_data.yaml", "r", "utf-8")
    document = fp.read()
    fp.close()

    # 将yaml格式内容 转换成 dict类型
    load = yaml.load_all(document)

    # 遍历迭代器
    for data in load:
        print(type(data))
        print(data)

        print("---" * 25)
        # 将python对象转换成为yaml格式文档
        output = yaml.dump(data)
        print(type(output))
        print(output)