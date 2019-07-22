#-*- coding:utf-8 -*-


__author__ = "苦叶子"

from flask import Flask
from flask import jsonify
from flask import request, Response
import random
import time

app = Flask(__name__)

"""
    这里所有的接口我们才去返回json串
    所有的json传对应的value值都为随机的
"""

# 生成随机字符串
def random_str():
    # 待选随机数据
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"

    # 用时间来做随机播种
    random.seed(time.time())

    # 随机选取数据
    sa = []
    for i in range(8):
        sa.append(random.choice(data))
    salt = ''.join(sa)

    return salt

# 构建response
def make_response():
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'

    return resp


# http GET
@app.route("/query", methods=["GET"])
def query():
    print("///////////////////////////")
    return jsonify(
        username=random_str(),
        password=random_str()
        )

# http POST
@app.route("/update", methods=["POST"])
def update():
    
    return make_response()


# http delete
@app.route("/delete", methods=["DELETE"])
def delete():
    
    return make_response()

# http head
@app.route("/head", methods=["HEAD"])
def head():
    
    return make_response()    

if __name__ == "__main__":

    app.run(debug=True)