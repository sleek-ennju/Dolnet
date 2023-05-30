#!/usr/bin/env python3
"""The user model module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


Base = declarative_base()


class User(Base):
    """The User class model representation"""
    __tablename__ = "users"
    user_id = Column(Integer, auto_increment=True, nullable=False)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), primary_key=True, nullable=False)
    user_phrase = Column(String(255), nullable=True)
    password = Column(String(255), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.utcnow)
