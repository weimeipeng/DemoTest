import flask,json
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

server.run(port=8888,debug=True,host='0.0.0.0')
