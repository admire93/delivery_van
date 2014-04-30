# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, UnicodeText, Unicode, DateTime
from sqlalchemy.orm import relationship

from .db import Base


__all__ = 'Album', 'Artist',


class Album(Base):
    """ 새로나오는 앨범들
    """

    id = Column(Integer, primary_key=True)

    name = Column(UnicodeText, nullable=False)

    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)

    artist = relationship('Artist')

    cover = Column(Unicode)

    link = Column(Unicode)

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    __tablename__ = 'albums'


class Artist(Base):
    """ 앨범에 적힌 아티스트
    """

    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)

    name = Column(UnicodeText, nullable=False)

    link = Column(Unicode)

    albums = relationship('Album', order_by="desc(Album.created_at)",
                          lazy='dynamic')

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    @property
    def first_album(self):
        albums = self.albums.limit(1).all()
        if not albums:
            return None
        return albums[0]
