# coding:utf-8

from flask import Flask
from app.action.auth import auth
from app.action.user import user
from app.action.product import product
from flask.templating import render_template

app_run = Flask(__name__)

###  register_blueprint 这个函数接受的参数是BluePrint 的对象
app_run.register_blueprint(user, url_prefix='/user')
app_run.register_blueprint(auth, url_prefix='/auth')
app_run.register_blueprint(product, url_prefix='/product')

#设置调试为true，可以不用重启既可以
app_run.debug = True

@app_run.route('/index')
def index():
    return render_template('index.html', name='qiwanren')  ### name 为传入的参数，默认取templates包下的文件

if __name__ == '__main__':
    app_run.run(host='0.0.0.0',port='8080')   ## 设置访问的ip和端口