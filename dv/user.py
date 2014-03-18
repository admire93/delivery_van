# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime

from .db import Base


__all__ = 'User', 'LoveArtist',


class User(Base):

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    fb_id = Column(Unicode, nullable=False)

    love_artists = relationship('LoveArtist',
                                primaryjoin='User.id==LoveArtist.user_id',
                                secondary='artists',
                                secondaryjoin='Artist.id==LoveArtist.artist_id')

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

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
