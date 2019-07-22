import yaml

if __name__== "__main__":
    document = """
    测试内容：Python 解析Yaml
    基本信息：
        姓名：韦鹏
        年龄：19
        性别：男
        id:29283833
    """
    load = yaml.load_all(document)
    for data in load:
        print(type(data))
        print(data)

        output = yaml.dump(data)
        print(output)
        print(type(output))