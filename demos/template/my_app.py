# -*- coding: utf-8 -*-
# python2默认使用ASCII编码，需要加上这个
from flask import Flask, render_template, Markup, flash, redirect, url_for, abort
import os

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route("/watchlist")
def my_watchlist():
    return render_template("my_watchlist.html", user=user, movies=movies)


@app.route('/')
def index():
    return render_template('my_index.html')


@app.context_processor
def inject_foo():
    return dict(foo='I am foo!')


@app.template_global()
def bar():
    return 'I am a bar.'


@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')


@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    else:
        return False


@app.route('/watchlist2')
def watchlist_with_static():
    return render_template('my_watchlist_with_static.html', user=user, movies=movies)


@app.route('/flash')
def just_flash():
    # python2需要加上u
    flash(u'我是闪电松鼠，谁在找我，我将终结他的生命')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/my_404.html', e=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/my_500.html', e=e), 500

@app.route('/trigger500')
def trigger500():
    abort(500)

@app.route('/trigger404')
def trigger404():
    abort(404)

