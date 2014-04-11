# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request

from ..album import Album
from ..db import session

bp = Blueprint('album', __name__, template_folder='templates/album')


@bp.route('/', methods=['GET'])
def all():
    page = request.args.get('page', 1, type=int)
    PAGE_PER_ARTIST = 15
    o = (page - 1) * PAGE_PER_ARTIST
    albums = session.query(Album)\
             .order_by(Album.created_at)\
             .offset(o)\
             .limit(PAGE_PER_ARTIST)\
             .all()
    return render_template('all.html', albums_=albums)
