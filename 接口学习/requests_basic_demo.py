#-*- coding:utf-8 -*-

__author__ = "苦叶子"


# 导入模块
import requests

if __name__ == "__main__":
    print("开源优测 - requests基本示例")

    # 发送HTTP GET请求，获取github API列表
    r = requests.get("https://api.github.com")

    # 请求返回码
    status_code = r.status_code

    # 完整的返回头
    headers = r.headers

    # 请求返回头 content-type的值
    content_type = r.headers["content-type"]

    # 返回内容编码类型
    code = r.encoding

    # 返回内容文本
    text = r.text

    # 若返回结果为json格式，我们可以获取其json格式内容
    json_data = r.json()

    # 打印上述所有获取到的值
    print("状态码： ", status_code)
    print("返回头： ", headers)
    print("content-type： ", content_type)
    print("编码：", code)
    print("文本内容： ", text)
    print("json串内容: ", json_data)
    