# -*- coding:utf-8 -*-

# じゃんけんプログラムの改良
import os
import random
import bottle
import jinja2
from bottle import get, post, request, route, run
from bottle import TEMPLATE_PATH, jinja2_template as template
# じゃんけんのためのクラスと関数
from functions2 import Hand, show_hands, referee

# test.pyが設置されているディレクトリの絶対パスを取得。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/template")


@get('/')
def h():
    return '''
        <form action="/rsp" method="post">
            名前を入力してください <input name="name" type="text" />
            どの手をだしますか？ グー：０、チョキ：１、パー：２ <input name="hand" type="text" />
            <input value="決定" type="submit" />
        </form>
    '''

@post('/rsp')
def r():

    your_name = request.forms.get('name')
    your_hand = request.forms.get('hand')
    your_hand = int(your_hand)

    # 
    # 操作部
    # 

    you = Hand(your_name, your_hand)

    
    machin = Hand("CPU", random.randint(0, 2))

    # だれがどの手を出したのか文章に起こす
    result1 = show_hands(you, machin)

    # どちらが勝ったのか文章に起こす
    result2 = referee(you, machin)

    # 表示するための結果を合成する
    results = [result1, result2]

    # return result
    return template('rsp_result.j2', results=results)

run(host='localhost', port=1046, debug=True)
