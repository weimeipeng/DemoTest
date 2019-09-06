#5-4 Yaml数据转化
#数据转化：dump()可以将Python对象序列化成为yaml流。
#如果stream为None，则返回生成的字符串。

#导入yaml模块：
import yaml

slogan=['welcome','to','alibaba']
website={'url':'https://job.alibaba.com/zhaopin/index.htm'}

#python data
print(slogan)
print(website)

#yaml data
print(yaml.dump(slogan))
print(yaml.dump(website))


