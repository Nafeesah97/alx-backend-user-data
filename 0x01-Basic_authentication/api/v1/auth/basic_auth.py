#!/usr/bin/env python3
""" Module of Basic Auth
"""
from ast import Return
from typing import Set, Union, TypeVar, Tuple
from api.v1.auth.auth import Auth
import base64
from models.user import User
import re


class BasicAuth(Auth):
    """
    A basic authentication class
    Methods:
    int
    str
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if (
                authorization_header is None or
                not isinstance(authorization_header, str)):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string"""
        if (
                base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded = (
                    base64.b64decode(
                        base64_authorization_header).decode('utf-8')
                    )
            return decoded
        except Exception as e:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str,
            ) -> Tuple[str, str]:
        """Extracts user credentials from a base64-decoded authorization
        header that uses the Basic authentication flow.
        """
        if type(decoded_base64_authorization_header) == str:
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')
                return user, password
        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if (
                user_email is None or
                not isinstance(user_email, str)):
            return None
        if (
                user_pwd is None or
                not isinstance(user_pwd, str)):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if users is None:
            return None

        if len(users) <= 0:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request"""
        if request is None:
            return None
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None
        base64_authorization_header = (
            self.extract_base64_authorization_header(authorization_header))
        if base64_authorization_header is None:
            return None
        decoded_base64_authorization_header = (
            self.decode_base64_authorization_header(
                base64_authorization_header))
        if decoded_base64_authorization_header is None:
            return None
        user_email, user_pwd = (
            self.extract_user_credentials(decoded_base64_authorization_header)
        )
        if user_email is None or user_pwd is None:
            return None
        return self.user_object_from_credentials(user_email, user_pwd)
