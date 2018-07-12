from bottle import route, run, template

@route('/hello/name')
def hello(name='Stranger'):
    return template("Hello {{name}} how are you doing?", name=name)

run(host='localhost', port=8080, debug=True)