#!/usr/bin/env python3
"""
filtered logger
Author: Nafeesah
"""
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """
    returns the log message obfuscated
     Args:
      fields: List of field names to obfuscate.
      redaction: String to replace sensitive data.
      message: The log message string.
      separator: Character separating fields in the message.

    Returns:
      The obfuscated log message
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
