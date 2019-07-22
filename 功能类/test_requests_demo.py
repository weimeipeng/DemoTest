#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import pytest
import requests

# 基于pytest requests测试 接口

class TestRequestDemo:
    # 初始化
    url = "http://jsonplaceholder.typicode.com"
    session = requests.session()

    # 测试获取所有用户信息接口 
    def test_get_posts(self):
        r = self.session.get(self.url + "/posts")
        
        # 断言状态码
        assert r.status_code == 200
        

        # 断言响应头信息
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"

        # 断言用户总数
        assert len(r.json()) == 100
    
    # 测试获取指定用户信息接口
    def test_get_posts_by_id(self):
        r = self.session.get(self.url + "/posts/1")

        # 断言状态码
        assert r.status_code == 200
        
        # 断言响应头信息
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"

        # 验证用户id
        data = r.json()
        assert data["userId"] == 1
        

    # 测试删除指定用户信息接口
    def test_delete_posts_by_id(self):
        r = self.session.delete(self.url + "/posts/1")

        # 断言状态码
        assert r.status_code == 200
        
        # 断言响应头信息
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"
        