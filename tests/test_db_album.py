# -*- coding: utf-8 -*-
from dv.album import Album
from dv.bugs import BugsRecentAlbum
from dv.db import session


def test_album(f_session):
    album = Album(name='9', artist='Damien Rice')
    session.add(album)
    session.commit()
    finded = session.query(Album).one()
    assert finded
    assert finded.id
    assert finded.name
    assert album.name == finded.name
    assert finded.artist
    assert album.artist == finded.artist


def test_save_album(f_session, f_page):
    bugs = BugsRecentAlbum()
    bugs.doc[1] = f_page
    for album in bugs.newest:
        session.add(Album(name=album['album_name'],
                          cover=album['thumbnail'],
                          link=album['album_link'],
                          artist=album['artist_name'],
                          artist_link=album['artist_link']))
    session.commit()
    albums = session.query(Album).all()
    assert len(bugs.newest) == len(albums)
    for album in bugs.newest:
        f = session.query(Album)\
            .filter(Album.name == album['album_name'])\
            .filter(Album.artist == album['artist_name'])\
            .all()
        assert f
        print album
        assert album['album_name'] == f[0].name
