# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template

from ..album import Artist
from ..db import session

bp = Blueprint('artist', __name__, template_folder='templates/artist')


@bp.route('/', methods=['GET'])
def all():
    artists = session.query(Artist)\
              .all()
    return render_template('all.html', artists=artists)


@bp.route('/', methods=['POST'])
def add():
    name = request.form.get('name', None)
    if not name:
        abort(400)
    artist = session.query(Artist)\
             .filter(Artist.name == name)\
             .all()
    if not artist:
        artist = Artist(name=name)
        session.add(artist)
        try:
            session.commit()
            return '201 added'
        except IntigrityError:
            session.rollback()
            abort(500)
    return '200 added'
