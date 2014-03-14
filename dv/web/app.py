# -*- coding: utf-8 -*-
from flask import Flask, url_for

from . import facebook_login, error
from .facebook_login import oauth
from .login import is_logined
from ..db import session, ensure_shutdown_session

app = Flask(__name__)

app.register_blueprint(facebook_login.bp, url_prefix='/fb')
app.register_blueprint(error.bp, url_prefix='/error')

oauth.init_app(app)

@app.route('/', methods=['GET'])
def home():
    if is_logined():
        return 'logined'
    else:
        return '<a href=%s>login</a>' % url_for('facebook_login.login')


ensure_shutdown_session(app)
