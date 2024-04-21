#!/usr/bin/env python3
""" Module of Auth
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
        for excluded_path in excluded_paths:
            if excluded_path.endswith("*") and path.startswith(
                excluded_path[:-1]):
                return False
            elif path == excluded_path or path == excluded_path[-1]:
                return False

            return True

    def authorization_header(self, request=None) -> str:
        """add authorization credentials"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """assert current user"""
        return None
