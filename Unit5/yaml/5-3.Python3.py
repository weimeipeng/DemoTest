#5-3 Yaml数据读取
#load方法：load(stream,Loader=Loader)解析文件流中的第一个yaml文档并生成相应的Python对象；

#导入yaml的模块：
import yaml

file=open('familyInfo.yaml',encoding='utf-8')
data=yaml.load(file,Loader=yaml.Loader)  #读取yaml里面的文件：
print(data)

print(data['name'])
print(data['age'])

print(data['spouse'])
print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'])
print(data['children'][0]['name'])
print(data['children'][0]['age'])

print(data['children'][1]['name'])
print(data['children'][1]['age'])

data['name']='51test'
print(data['name'])



