# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

from ..album import Album
from ..db import session

bp = Blueprint('album', __name__, template_folder='templates/album')


@bp.route('/', methods=['GET'])
def all():
    albums = session.query(Album)\
             .order_by(Album.created_at)\
             .all()
    return render_template('all.html', albums_=albums)
