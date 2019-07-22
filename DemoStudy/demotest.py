import requests

if __name__ == '__main__':

    r =requests.get("http://localhost:5000/getmysql")
    status_code = r.status_code
    headers = r.headers
    content_type = r.headers["content-type"]     
    print("状态码： ", status_code)
    print("返回头： ", headers)
    print("content-type： ", content_type)
    print("编码：", r.encoding)
    print("文本内容： ", r.text)
    print("json串内容: ", r.json)