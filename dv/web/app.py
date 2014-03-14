# -*- coding: utf-8 -*-
from flask import Flask, url_for, g, redirect

from . import facebook_login, error
from .facebook_login import oauth
from .login import is_logined, need_login
from ..db import session, ensure_shutdown_session

app = Flask(__name__)

app.register_blueprint(facebook_login.bp, url_prefix='/fb')
app.register_blueprint(error.bp, url_prefix='/error')

oauth.init_app(app)

@app.route('/', methods=['GET'])
def home():
    user = is_logined()
    if user:
        return redirect(url_for('u', user_id=user.id))
    else:
        return '<a href=%s>login</a>' % url_for('facebook_login.login')


@app.route('/user/<int:user_id>/')
@need_login
def u(user_id):
    return 'Hello %s' % g.current_user.name


ensure_shutdown_session(app)
