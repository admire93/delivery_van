# -*- coding: utf-8 -*-
from pytest import fixture

from dv.user import LoveArtist, ReadAlbum
from dv.album import Album


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


def test_read_album(f_session, f_user, f_album):
    ra = ReadAlbum(user=f_user, album=f_album)
    f_session.add(ra)
    f_session.commit()
    assert ra
    assert f_user.id == ra.user_id
    assert f_album.id == ra.album_id


def test_user_read_album(f_session, f_user, f_album):
    ra = ReadAlbum(user=f_user, album=f_album)
    f_session.add(ra)
    f_session.commit()
    assert f_user.latest_readed_album
    assert f_user.latest_readed_album.id


@fixture
def f_read_album(f_session, f_user, f_album):
    ra = ReadAlbum(user=f_user, album=f_album)
    f_session.add(ra)
    f_session.commit()
    return ra


def test_user_do_read_album(f_session, f_user, f_album):
    assert not f_user.latest_readed_album
    f_user.read_album(f_album.id)
    assert f_user.latest_readed_album
    assert f_album.id == f_user.latest_readed_album.id


def test_user_do_read_album_without_id(f_session, f_user, f_album, f_artist):
    love = LoveArtist(artist=f_artist, user=f_user)
    f_session.add(love)
    f_session.commit()
    assert love
    assert not f_user.latest_readed_album
    f_user.read_album()
    assert f_user.latest_readed_album


def test_user_twice_read_album(f_session, f_user, f_album, f_artist):
    nine = Album(name=u'9', artist=f_artist)
    f_session.add(nine)
    f_session.commit()
    f_user.read_album(f_album.id)
    f_user.read_album(nine.id)
