# -*- coding: utf-8 -*-
from flask import Blueprint, url_for, g, render_template, abort

from .login import need_login
from ..user import User
from ..db import session

bp = Blueprint('user', __name__, template_folder='templates/user')

@bp.route('/<int:user_id>/', methods=['GET'])
@need_login
def user(user_id):
    user = session.query(User)\
           .filter(User.id == user_id)\
           .all()
    if not user:
        abort(400)
    return render_template('index.html', user=user[0])
