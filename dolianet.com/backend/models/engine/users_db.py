#!/usr/bin/env python3
"""User module to handle all User methods"""
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from models.user import User
from models.engine.db import DB
from datetime import datetime

class Users(DB):
    """User class that contains all user methods"""
    def __init__(self) -> None:
        """Init method for class Users"""
        super().__init__()

    def create_user(self, user_id: int, user_name: str, user_phrase: str, 
                    email: str, password: str) -> User:
        """Method to create a User"""
        try:
            user = User(user_id=user_id, user_name=user_name, user_phrase=user_phrase, 
                        email=email, password=password)
            self._session.add(user)
            self._session.commit()
            return user
        except Exception as err:
            self._session.rollback()
            print(err)
            return None

    def find_user_by(self, **kwargs) -> User:
        """Find user from DB by key-value pairs argument"""
        if not kwargs or not self.valid_query_args_user(**kwargs):
            raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).one_or_none()

        if not user:
            raise NoResultFound
        return user

    def find_user_id(self, email: str) -> User:
        """Get user details by using email"""
        user = self.find_user_by(email=email)
        if not user:
            raise NoResultFound
        user_details = {}
        for key, value in user.__dict__.items():
            user_details[key] = str(value)
            if '_sa_instance_state' in user_details:
                del user_details['_sa_instance_state']
        return user_details

    def update_user(self, email: str, **kwargs) -> None:
        """Update user details based on email"""
        try:
            if not self.valid_query_args_user(**kwargs):
                raise ValueError
            user = self.find_user_by(email=email)
            if not user:
                raise NoResultFound
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.date_updated = datetime.now()
            self._session.commit()
        except Exception as err:
            self._session.rollback()
            return False
        return True

    def valid_query_args_user(self, **kwargs):
        """Get table columns or keys"""
        columns = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in columns:
                return False
        return True

    def all_users(self) -> List[User]:
        """Returns all users registered on the platform"""
        objs = []
        users = self._session.query(User).order_by(User.user_id)
        for user in users:
            obj = user.__dict__.copy()
            if obj['_sa_instance_state']:
                del obj['_sa_instance_state']
            objs.append(obj)
        return objs
 
