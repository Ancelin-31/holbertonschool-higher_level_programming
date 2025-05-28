#!/usr/bin/python3
"""Determines if an object belongs to a class"""


def is_same_class(obj, a_class):
    """Returns True if obj belongs to a_class, otherwise returns false"""

    if isinstance(obj, a_class):
        return True

    else:
        return False
