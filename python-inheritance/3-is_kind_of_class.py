#!/usr/bin/python3
"""Determines if an object belongs to a class or a subclass"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj belongs to a class or subclass,
    otherwise returns false"""

    if isinstance(obj, a_class):
        return True

    else:
        return False
