#!/usr/bin/env python3
"""
filtered logger
"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    pattern = r"(?:{separator})".format(separator=separator)
    for field in fields:
        pattern += r"(?:" + field + r"\=)([^;]+)"
        pattern += r"(?|{separator})".format(separator=separator)

    return re.sub(pattern, redaction, message)
