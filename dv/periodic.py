# -*- coding: utf-8 -*-
from threading import Timer

from .album import Album, Artist
from .db import session


def do(f, time, *args):
    f(*args)
    Timer(time, lambda: do(f, time, *args)).start()


def save_albums(bugs_newest):
    for bugs in bugs_newest:
        artists = session.query(Artist)\
                  .filter(Artist.name == bugs['artist_name'])\
                  .all()
        if not artists:
            artist = Artist(name=bugs['artist_name'], link=bugs['artist_link'])
            session.add(artist)
        else:
            artist = artists[0]
        album = Album(artist=artist,
                      name=bugs['album_name'],
                      link=bugs['album_link'],
                      cover=bugs['thumbnail'])
        session.add(album)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            raise
