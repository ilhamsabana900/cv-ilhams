import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mypage')
def mypage():
    return 'this is page'

@app.route('/test', methods =['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)

    return jsonify({
        'result' : 'success',
        'msg' : 'GET this request!'
    })

@app.route('/test', methods =['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)

    return jsonify({
        'result' : 'success',
        'msg' : 'request is POST'
    })

# @app.route('/test', methods=['POST'])
# def test_post():
#     title_receive = request.form['title_give']
#     print(title_receive)
#     return jsonify({
#         'result':'success', 
#         'msg': 'This request is POST!'
#     })
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000,debug=True)