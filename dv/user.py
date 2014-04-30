# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime

from .db import Base, Session


__all__ = 'User', 'LoveArtist', 'ReadAlbum'


class User(Base):

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    fb_id = Column(Unicode, nullable=False)

    love_artists = relationship('Artist', secondary='love_artists')

    # love_albums

    latest_readed_album = relationship('Album',
                                       secondary='read_albums',
                                       uselist=False)

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    def read_album(self, id=-1, commit=True):
        from .album import Album
        session = Session.object_session(self)
        if id == -1:
            latest_albums = session.query(Album)\
                            .join(LoveArtist,
                                  LoveArtist.artist_id == Album.artist_id)\
                            .filter(LoveArtist.user_id == self.id)\
                            .order_by(Album.created_at.desc())\
                            .limit(1)\
                            .all()
            if latest_albums:
                id = latest_albums[0].id
        ra = ReadAlbum(user=self, album_id=id)
        session.add(ra)
        if commit:
            session.commit()

    __tablename__ = 'users'


class LoveArtist(Base):

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)

    user = relationship('User')

    artist = relationship('Artist')

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    __tablename__ = 'love_artists'


class ReadAlbum(Base):
    """ 유저가 자신이 읽은 앨범 들을 확인합니다
    """

    __tablename__ = 'read_albums'

    album_id = Column(Integer, ForeignKey('albums.id'))

    album = relationship('Album')

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    user = relationship('User')
