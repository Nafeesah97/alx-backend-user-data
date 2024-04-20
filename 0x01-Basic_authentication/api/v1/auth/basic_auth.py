#!/usr/bin/env python3
""" Module of Basic Auth
"""
from typing import Set, Union, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User

class BasicAuth(Auth):
    """
    A basic authentication class
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
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """It is used to extract credentials"""
        if (
                decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return tuple(decoded_base64_authorization_header.split(":"))

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
        user = User.search({'email': user_email})
        
        if user is None:
            return None
        
        if not user.is_valid_password(user_pwd):
            return None
        
        return user        
