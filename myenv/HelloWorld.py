
from bottle import route, run


@route('/hello')
def hello():
    return "Hello World!"


run(host='localhost', port=1046, debug=True, relorder=True)