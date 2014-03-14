# -*- coding: utf-8 -*-
from hashlib import sha256
from datetime import datetime
from functools import wraps

from flask import current_app, json, g, session as web_session

from ..db import session
from ..user import User


def generate_checksum(payload):
    secret = current_app.config['SECRET_KEY']
    l = json.dumps(payload)
    return sha256(l + secret).hexdigest()


def get_token(user):
    payload = {'id': user.id, 'logined_at': datetime.now()}
    r = '%s.%s' % (json.dumps(payload), generate_checksum(payload))
    return r.encode('base64')


def get_token_from_encoded(encoded):
    decoded = encoded.decode('base64')
    payload, checksum = decoded.split('.')
    payload = json.loads(payload)
    return payload, checksum


def validate(token):
    # TODO: validate date
    try:
        payload, checksum = get_token_from_encoded(token)
        g_checksum = generate_checksum(payload)
        return payload
    except:
        return False


def is_logined():
    token = web_session.get('dv_token', None)
    if token:
        p = validate(token)
        user = session.query(User)\
               .filter(p['id'])\
               .all()
        if user:
            return user
    return False


def need_login(f)
    @wraps(f)
    def deco(*args, **kwargs):
        user = is_logined()
        if user:
            g.current_user = user
            f(*args, **kwargs)
        else:
            abort(400)
    return deco
