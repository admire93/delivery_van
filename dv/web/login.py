# -*- coding: utf-8 -*-
from flask import session as web_session

def get_token(user):
    return 'abc'


def validate(token):
    return True


def is_logined():
    token = web_session.get('dv_token', None)
    return token and validate(token)
