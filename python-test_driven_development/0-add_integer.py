#!/usr/bin/python3

def add_integer(a, b=98):
    """
Adds two integers or floats, casting them to integers if necessary.

    Args:
        a: The first number (must be an integer or float).
        b: The second number (must be an integer or float, default is 98).

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b is not an integer or float.
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
