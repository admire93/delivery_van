# -*- coding: utf-8 -*-
from flask import json
from sqlalchemy.orm import contains_eager

from dv.user import User, LoveArtist
from dv.web.app import app

from ..util import url_for


def test_web_love_artist(f_artist, f_user, f_token, f_session):
    url = url_for('user.add_love_artist', user_id=f_user.id, token=f_token)
    with app.test_client() as c:
        r = c.post(url, data={'artist_name': f_artist.name})
    assert 302 == r.status_code
    user = f_session.query(User)\
           .options(contains_eager(User.love_artists))\
           .filter(User.id == f_user.id)\
           .all()
    assert user
    assert user[0].love_artists


def test_web_not_duplicate_love_artist(f_artist, f_user, f_token, f_session):
    url = url_for('user.add_love_artist', user_id=f_user.id, token=f_token)
    with app.test_client() as c:
        r = c.post(url, data={'artist_name': f_artist.name})
        r = c.post(url, data={'artist_name': f_artist.name})
    user = f_session.query(User)\
           .options(contains_eager(User.love_artists))\
           .filter(User.id == f_user.id)\
           .all()
    assert user
    assert user[0].love_artists
    assert 1 == len(user[0].love_artists)


def test_web_is_love_artist(f_artist, f_user, f_token, f_session):
    url = url_for('user.add_love_artist', user_id=f_user.id, token=f_token)
    with app.test_client() as c:
        r = c.post(url, data={'artist_name': f_artist.name})
    artist_ids = [f_artist.id, 123, 456]
    a = ','.join(map(lambda x: str(x), artist_ids))
    url = url_for('user.is_love_artist',
                  user_id=f_user.id,
                  token=f_token,
                  artist_ids=a)
    with app.test_client() as c:
        r = c.get(url)
    assert 200 == r.status_code
    data = json.loads(r.data)
    assert 'artist_ids' in data
    assert 1 == len(data['artist_ids'])
    assert f_artist.id in data['artist_ids']
