# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, url_for, session as web_session

bp = Blueprint('error', __name__, template_folder='templates/error')

@bp.route('/fail/', methods=['GET'])
def failed():
    return 'fail page.'
