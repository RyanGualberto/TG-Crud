"""Post model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, Float
from sqlalchemy.orm import relationship, backref
from datetime import datetime

from postsapi.model import DeclarativeBase, metadata, DBSession


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    body = Column(UnicodeText, nullable=False)
    author = Column(Unicode(255), nullable=False)
    created = Column(DateTime, default=datetime.now)

    def get_all(self):
        return DBSession.query(Post).all()


__all__ = ['Post']
