# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, UnicodeText, Unicode, DateTime

from .db import Base


class Album(Base):

    id = Column(Integer, primary_key=True)

    name = Column(UnicodeText, nullable=False)

    artist = Column(Unicode, nullable=False)

    cover = Column(Unicode)

    link = Column(Unicode)

    artist_link = Column(Unicode)

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    __tablename__ = 'albums'
