#!/usr/bin/env python3
""" Module of Basic Auth
"""
from typing import Set, Union
from api.v1.auth.auth import Auth
import base64


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
            ) -> tuple(str, str):
        """It is used to extract credentials"""
        if (
                decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return (None, None)        
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return tuple(decoded_base64_authorization_header.split(":"))
