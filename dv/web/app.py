# -*- coding: utf-8 -*-
from flask import Flask, url_for, g, redirect

from . import facebook_login, error, user, artist, album
from .facebook_login import oauth
from .login import is_logined
from ..db import session, ensure_shutdown_session

app = Flask(__name__)

app.register_blueprint(facebook_login.bp, url_prefix='/fb')
app.register_blueprint(error.bp, url_prefix='/error')
app.register_blueprint(user.bp, url_prefix='/users')
app.register_blueprint(artist.bp, url_prefix='/artists')
app.register_blueprint(album.bp, url_prefix='/albums')

oauth.init_app(app)


@app.template_filter('is_login')
def template_login(s):
    if s is None:
        return is_logined()
    return s


@app.route('/', methods=['GET'])
def home():
    user = is_logined()
    if user:
        return redirect(url_for('user.user', user_id=user.id))
    else:
        return '<a href=%s>login</a>' % url_for('facebook_login.login')


ensure_shutdown_session(app)
