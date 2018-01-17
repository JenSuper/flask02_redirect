#encoding: utf-8
from flask import Flask,redirect,url_for
'''
访问quest时
1. 如果为登录状态，则跳转到主页面
2. 如果不是登录状态，则跳转到登录页面
'''
app = Flask(__name__)

@app.route('/')
def index():
    return u'主页面'

@app.route('/login')
def login():
    return u'登录页面'

@app.route('/quest/<is_login>')
def question(is_login):
    if is_login == '1':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
