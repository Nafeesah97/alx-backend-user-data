#!/usr/bin/env python3
""" Module of Index views
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authorization class
    Method:
        require_auth(path, excluded_paths): returns False
        authorization_header(request): returns None
        current_user(request): returns None
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """to require authorization"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path.endswith("/"):
            path = path
        else:
            path = path + "/"
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """add authorization credentials"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """assert current user"""
        return None
