# -*- coding: utf-8 -*-
from flask import (Blueprint, jsonify, url_for, request, redirect,
                   session as web_session)
from flask_oauthlib.client import OAuth

from ..user import User
from ..db import session
from .login import get_token


bp = Blueprint('facebook_login',
               __name__,
               template_folder='templates/facebook_login')

oauth = OAuth()

fb = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    request_token_params={'scope': 'email'},
    access_token_url='https://graph.facebook.com/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    app_key='FACEBOOK'
)


@bp.route('/login/', methods=['GET'])
def login():
    return fb.authorize(callback=url_for('.authorized', _external=True))


@bp.route('/login/authorized/', methods=['GET'])
@fb.authorized_handler
def authorized(resp):
    if resp is None or 'access_token' not in resp:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    web_session['fb_token'] = (resp['access_token'], '')
    resp = fb.get('me', data={'locale': 'ko_KR'})
    if resp.status == 200:
        me = resp.data
        user = User(name=me['name'], fb_id=me['id'])
        session.add(user)
        session.commit()
        web_session['dv_token'] = get_token(user)
        return redirect(url_for('home'))
    return redirect('error.failed')


@fb.tokengetter
def get_fb_token():
    return web_session.get('fb_token')


@bp.route('/logout/', methods=['GET'])
def logout():
    web_session.pop('fb_token', None)
    web_session.pop('dv_token', None)
    return redirect(url_for('home'))
