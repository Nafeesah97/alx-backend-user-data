#!/usr/bin/env python3
"""auth
module"""
import bcrypt
from user import User
from db import DB


def _hash_password(password: str) -> bytes:
    """hashes a password to a salt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """To register a new user"""
        if self._db.find_user_by(email=email):
            raise ValueError, f"User {email} already exists"
        else:
            pw = _hash_password(password)
            new_user = self._db.add_user(email, pw)
            return new_user
