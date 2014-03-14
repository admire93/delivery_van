# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from .db import Base


class User(Base):

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    fb_id = Column(Unicode, nullable=False)

    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)

    __tablename__ = 'users'
