# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, UnicodeText, Unicode, DateTime
from sqlalchemy.orm import relationship

from .db import Base


__all__ = 'Album', 'Artist',


class Album(Base):

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

    id = Column(Integer, primary_key=True)

    name = Column(UnicodeText, nullable=False)

    link = Column(Unicode)

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    __tablename__ = 'artists'
