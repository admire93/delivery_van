# -*- coding: utf-8 -*-
from pytest import fixture

from dv.album import Album, Artist
from dv.bugs import BugsRecentAlbum


def test_artist(f_session):
    artist_name = 'Damien Rice'
    a = Artist(name=artist_name)
    assert a
    f_session.add(a)
    f_session.commit()
    finded = f_session.query(Artist)\
             .filter(Artist.name == artist_name)\
             .all()
    assert finded
    damien = finded[0]
    assert a.name == damien.name
    assert damien.created_at


@fixture
def f_artist(f_session):
    damien = Artist(name='Damien Rice')
    f_session.add(damien)
    f_session.commit()
    return damien


def test_album(f_artist, f_session):
    album = Album(name='9', artist=f_artist)
    f_session.add(album)
    f_session.commit()
    finded = f_session.query(Album).one()
    assert finded
    assert finded.id
    assert finded.name
    assert album.name == finded.name
    assert album.artist
    assert f_artist.name == album.artist.name


def test_save_album(f_session, f_page):
    bugs = BugsRecentAlbum()
    bugs.doc[1] = f_page
    for album in bugs.newest:
        artist = Artist(name=album['artist_name'], link=album['artist_link'])
        f_session.add(artist)
        f_session.add(Album(name=album['album_name'],
                            cover=album['thumbnail'],
                            link=album['album_link'],
                            artist=artist))
    f_session.commit()
    albums = f_session.query(Album).all()
    assert len(bugs.newest) == len(albums)
    for album in bugs.newest:
        f = f_session.query(Album)\
            .filter(Album.name == album['album_name'])\
            .all()
        assert f
        assert album['album_name'] == f[0].name
        assert album['artist_name'] == f[0].artist.name
