from flask import Flask, redirect, abort,  make_response

app = Flask(__name__)

# the minimal Flask application


# bind multiple URL for one view function
@app.route('/')
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return redirect('https://www.baidu.com')


@app.route('/404')
def not_found():
    abort(418)


@app.route('/brew/<drink>')
def teapot(drink):
    if drink == 'coffee':
        abort(418)
    else:
        return 'A drop of tea.'


@app.route('/foo')
def foo():
    response = make_response("<h1>Hello World</h1>")
    response.mimetype = 'text/html'
    return response

