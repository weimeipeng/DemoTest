from flask import Flask,jsonify
import requests

app = Flask(__name__)


def make_response():
    # content = '{"result":"peirongqin","data":"19911012"}'
    # resp = Response(content)
    # resp.headers["Access-Control-Origin"] = '*'

    resp ="welcome to API"
    return resp

@app.route('/api')
def index():
    return "Hello,world!!!"

@app.route("/getmysql",methods=["GET"])
def getmysql():
    return jsonify(
        username = "weipeng",
        passoword ="123456"
    )

@app.route("/update",methods=["POST"])
def update():
    return make_response()



if __name__ == '__main__':
   app.run()
        