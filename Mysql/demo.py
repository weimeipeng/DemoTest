#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='test801')

cursor = db.cursor()
cursor.execute("select * from pre_common_member where username='000'")
data=cursor.fetchone()
print('数据库的版本为：',data)
db.close()