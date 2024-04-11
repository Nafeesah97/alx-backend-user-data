#!/usr/bin/env python3
"""
filtered logger
Author: Nafeesah
"""
import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialisation"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records """
        message = super(RedactingFormatter, self).format(record)
        text = filter_datum(
                self.fields, self.REDACTION, message, self.SEPARATOR)
        return text
