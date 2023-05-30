#!/usr/bin/env python3
"""The user model module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class User(Base):
    """The User class representation"""
    __tablename__ = "users"
    user_id = Column(Integer, auto_increment=True, nullable=False)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), primary_key=True, nullable=False)
    user_phrase = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
