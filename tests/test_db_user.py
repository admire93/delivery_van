# -*- coding: utf-8 -*-
from dv.user import LoveArtist


def test_love_artist(f_session, f_user, f_artist):
    love = LoveArtist(artist=f_artist, user=f_user)
    f_session.add(love)
    f_session.commit()
    assert love
    assert f_artist.id == love.artist.id
    assert f_user.id == love.user.id


def test_rel_love_artist(f_session, f_user, f_artist):
    love = LoveArtist(artist=f_artist, user=f_user)
    f_session.add(love)
    f_session.commit()
    assert love
    assert f_artist.id == love.artist.id
    assert f_user.id == love.user.id
    assert f_user.love_artists
    assert love.artist.id == f_user.love_artists[0].id
