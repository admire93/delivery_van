# -*- coding: utf-8 -*-
from sqlalchemy.orm import contains_eager

from dv.user import User, LoveArtist
from dv.web.app import app

from ..util import url_for


def test_web_love_artist(f_artist, f_user, f_token, f_session):
    url = url_for('user.add_love_artist', user_id=f_user.id, token=f_token)
    with app.test_client() as c:
        r = c.post(url, data={'artist_name': f_artist.name})
    assert 200 == r.status_code
    user = f_session.query(User)\
           .options(contains_eager(User.love_artists))\
           .filter(User.id == f_user.id)\
           .all()
    assert user
    assert user[0].love_artists
