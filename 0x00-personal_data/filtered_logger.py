#!/usr/bin/env python3
"""
filtered logger
"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    pattern = re.compile(r'({})(?={}|\Z)'.format('|'.join(fields), separator))
    return pattern.sub(redaction, message)
