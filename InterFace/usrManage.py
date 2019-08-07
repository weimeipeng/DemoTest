#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pymysql
import flask,json

db=pymysql.connect(host='172.31.128.199',user='root',password='root',port=3306,db='ecshop_new')

server = flask.Flask(__name__)
@server.route('/login',methods=['get'])
def login():
    res = {'msg':'这是我开发的第一个接口','msg_code':'0000'}
    name = flask.request.values.get('username')
    password = flask.request.values.get('password')

    if(name=="weipeng" and password=="123456"):
        res = {'msg':'登录成功','msg_code':'200'}
    else:
        res = {'msg':'登录失败','msg_code':'400'}
    return json.dumps(res,ensure_ascii=False)

@server.route('/userinfo',methods=['get'])
def userInfo():        #测试服务器 ecshop 信息查询接口
    name = flask.request.values.get('username')
    if(name!=None):
        sql = "select * from ecs_users where user_name = '%s'" % name
        print(sql)
    else:
        sql = 'select * from ecs_users'

    cursor = db.cursor()    #数据库连接
    db.ping(reconnect=True)  #检查数据库是否连接断开，如果连接中断，自动重新连接
    cursor.execute(sql)
    if(cursor.rowcount>0):   #判断查询结果是否为空
        data=cursor.fetchone()  #返回查询到的第一条记录
        userinfo={
        "error_code": 0,
        "message_info":"ok",
        "stu_info": [
            {
                "userid": data[0],
                "username": data[2],
                "password":data[3],
                "sex": "男",
                "email":data[1],
                "addr": "空",
                "regtime":data[13],
                "last_login":data[14],
                "last_ip":data[16],
                "phone":data[29],
                "birthday":str(data[7])
                }]}
        
    else:
        userinfo={
        "error_code": 404,
        "message_info":"NotFount",
        "stu_info": [
            {
                "userid": 0,
                "username": 0,
                "password":0,
                "sex": "男",
                "email":0,
                "addr": "空",
                "regtime":0,
                "last_login":0,
                "last_ip":0,
                "phone":0,
                "birthday":0
                }]}

    db.commit()
    db.close()
    
 #   userinfo='{"error_code": 0,"message_info":"ok","stu_info": [{"userid": %d,"username": "%s","password":"%s","sex": "男","email": "%s","addr": "空","regtime":"%s","status": %d}]}' % (data[0],data[2],data[3],data[1],data[12],data[4])
    return json.dumps(userinfo,indent=1,ensure_ascii=False)


@server.route('/usercount',methods=['get'])
def userCount():        #测试服务器 ecshop 查询注册用户数
    cursor = db.cursor()    #数据库连接
    db.ping(reconnect=True)
    cursor.execute('select count(*) from ecs_users')
    num=cursor.fetchone()  #返回查询到的第一条记录
    db.commit()
    db.close()
    
 #   userinfo='{"error_code": 0,"message_info":"ok","stu_info": [{"userid": %d,"username": "%s","password":"%s","sex": "男","email": "%s","addr": "空","regtime":"%s","status": %d}]}' % (data[0],data[2],data[3],data[1],data[12],data[4])
    userinfo={
        "error_code": 200,
        "message_info":"ok",
        "stu_info_count":num
        }

    return json.dumps(userinfo,indent=1,ensure_ascii=False)















server.run(port=8888,debug=True,host='0.0.0.0')

