#!/usr/bin/python3

"""
Returns the current date and time.
"""

from datetime import datetime


def get_date():
    """
    Returns the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M")
