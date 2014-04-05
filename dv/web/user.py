# -*- coding: utf-8 -*-
from flask import (Blueprint, url_for, g, render_template, abort, request,
                   redirect)
from sqlalchemy.orm import contains_eager
from sqlalchemy.exc import IntegrityError

from .login import need_login
from ..user import User, LoveArtist
from ..album import Artist, Album
from ..db import session

bp = Blueprint('user', __name__, template_folder='templates/user')

@bp.route('/me/', methods=['GET'])
@need_login
def me():
    return redirect(url_for('.user', user_id=g.current_user.id))


@bp.route('/<int:user_id>/', methods=['GET'])
@need_login
def user(user_id):
    user = session.query(User)\
           .filter(User.id == user_id)\
           .all()
    if not user:
        abort(404)
    is_me = (user[0].id == g.current_user.id)
    albums = session.query(Album)\
             .join(LoveArtist, LoveArtist.artist_id == Album.artist_id)\
             .filter(LoveArtist.user_id == user_id)\
             .order_by(Album.created_at.desc())\
             .limit(5)\
             .all()
    return render_template('index.html', user=user[0], me=is_me,
                           love_albums=albums)


@bp.route('/<int:user_id>/love_artists/', methods=['POST'])
@need_login
def add_love_artist(user_id):
    user = session.query(User)\
           .filter(User.id == user_id)\
           .all()
    if not user:
        abort(404)
    if user[0].id != g.current_user.id:
        abort(403)
    name = request.form.get('artist_name', None)
    if not name:
        abort(400)
    a = session.query(Artist)\
        .filter(Artist.name == name)\
        .all()
    if not a:
        artist = Artist(name=name)
        session.add(artist)
        love_artist = []
    else:
        artist = a[0]
        love_artist = session.query(LoveArtist)\
                      .filter(LoveArtist.artist_id == artist.id)\
                      .filter(LoveArtist.user_id == user[0].id)\
                      .all()
    if not love_artist:
        rel = LoveArtist(artist=artist, user=user[0])
        session.add(rel)
    try:
        session.commit()
    except IntegrityError as e:
        session.rollback()
        abort(500)
    return redirect(url_for('.love_artist', user_id=user[0].id))


@bp.route('/<int:user_id>/love_artists/', methods=['GET'])
@need_login
def love_artist(user_id):
    user = session.query(User)\
           .filter(User.id == user_id)\
           .all()
    return render_template('love_artist.html',
                           love_artists=user[0].love_artists)


@bp.route('/<int:user_id>/love_artists/<int:artist_id>/', methods=['POST'])
@need_login
def do_love_artist(user_id, artist_id):
    if g.current_user.id != user_id:
        abort(403)
    artist = session.query(Artist)\
             .filter(Artist.id == artist_id)\
             .all()
    if artist:
        g.current_user.love_artists.append(artist[0])
        session.add(g.current_user)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(500)
    # TODO: 아티스트 페이지로 다시 보내주기 (referer)
    return redirect(url_for('user.me'))


@bp.route('/<int:user_id>/love_albums/')
def love_album(user_id):
    albums = session.query(Album)\
             .join(LoveArtist, LoveArtist.artist_id == Album.artist_id)\
             .filter(LoveArtist.user_id == user_id)\
             .order_by(Album.created_at.desc())\
             .all()
    return render_template('love_album.html', love_albums=albums)
