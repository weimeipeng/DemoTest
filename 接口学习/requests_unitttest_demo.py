#-*- coding:utf-8 -*-

__author__ = "苦叶子"

import requests
import unittest

## 测试用例
class JsonPlaceTest(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.url = "http://jsonplaceholder.typicode.com"
        self.session = requests.session()

    # 测试获取所有用户信息接口 
    def test_get_posts(self):
        r = self.session.get(self.url + "/posts")
        
        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"], "application/json; charset=utf-8")

        # 断言用户总数
        self.assertEqual(len(r.json()), 100)
    
    # 测试获取指定用户信息接口
    def test_get_posts_by_id(self):
        r = self.session.get(self.url + "/posts/1")

        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"], "application/json; charset=utf-8")

        # 验证用户id
        data = r.json()
        self.assertEqual(data["userId"], 1)
        

    # 测试删除指定用户信息接口
    def test_delete_posts_by_id(self):
        r = self.session.delete(self.url + "/posts/1")

        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"], "application/json; charset=utf-8")
        

    # 清理
    def tearDown(self):
        if self.session:
            self.session.close()


if __name__ == "__main__":
    print("requests unittest接口测试实例")

    unittest.main()
        