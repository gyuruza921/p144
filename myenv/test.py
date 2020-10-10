import os
import bottle
import jinja2
from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template

# test.pyが設置されているディレクトリの絶対パスを取得。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/template")


@route('/hello/<name>')
def hello(name):
    return template('hello.j2', name=name)


run(host='localhost', port=1046, debug=True, reloader=True)