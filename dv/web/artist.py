# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, g

from ..album import Artist
from ..db import session
from .login import is_logined
from .util import pager

bp = Blueprint('artist', __name__, template_folder='templates/artist')


@bp.route('/', methods=['GET'])
def all():
    page = request.args.get('page', 1, type=int)
    name = request.args.get('name', u'', type=unicode)
    PAGE_PER_ARTIST = 15
    o = (page - 1) * PAGE_PER_ARTIST
    q = session.query(Artist)\
        .order_by(Artist.created_at)
    if name:
        q = q.filter(Artist.name.ilike(u'%{0}%'.format(name)))
    artists = q.offset(o)\
              .limit(PAGE_PER_ARTIST)\
              .all()
    return render_template('all_artist.html', artists=artists,
                           me=is_logined(),
                           pages=pager(page, q.count(), PAGE_PER_ARTIST))
