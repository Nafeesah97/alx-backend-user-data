#!/usr/bin/env python3
"""
filtered logger
"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    return re.sub(r'(?<=\b|{})({})(?=\b|{})'
                  .format(separator, '|'.join(fields), separator),
                  redaction, message)