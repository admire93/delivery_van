# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, g

from ..album import Artist
from ..db import session
from .login import is_logined

bp = Blueprint('artist', __name__, template_folder='templates/artist')


@bp.route('/', methods=['GET'])
def all():
    artists = session.query(Artist)\
              .all()
    print artists[0].first_album
    return render_template('all_artist.html', artists=artists,
                           me=is_logined())
