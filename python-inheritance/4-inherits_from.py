#!/usr/bin/python3
"""Determines if an object belongs to a class"""


def inherits_from(obj, a_class):
    """Returns True if obj belongs to a subclass, otherwise returns false"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True

    else:
        return False
