#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound as ORMNoResultFound


class DB:
    """DB class.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """To filter the user and return first row"""
        column = []
        row = []
        for key, value in kwargs.items():
            column.append(getattr(User, key))
            row.append(value)
        try:
            res = self.__session.query(User).filter(
                tuple_(*column).in_([tuple(row)])
            ).first()
            if res is None:
                raise NoResultFound()
            return res
        except ORMNoResultFound:
            raise NoResultFound()
        except InvalidRequestError as error:
            raise error
