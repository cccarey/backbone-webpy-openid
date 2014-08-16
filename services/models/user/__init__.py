from config import *

user_table = 'users'

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    password = Column(String(200), default='')
    first_name = Column(String(50))
    last_name = Column(String(50))
    nick_name = Column(String(50), default='')
    fullname = Column(String(100))
    email = Column(String(200))
    active = Column(Boolean, default=True)

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True
