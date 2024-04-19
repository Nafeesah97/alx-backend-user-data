#!/usr/bin/env python3
""" Module of Basic Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    A basic authentication class    
    """
    def __init__(self):
        super().__init__()