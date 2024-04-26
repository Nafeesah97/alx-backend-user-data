#!/usr/bin/env python3
"""auth
module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hashes a password to a salt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
