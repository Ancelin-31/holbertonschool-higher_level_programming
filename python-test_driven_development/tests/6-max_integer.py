#!/usr/bin/python3
"""Module to find the max integer in a list"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    max_value = list[0]
    for i in list:
        if i > max_value:
            max_value = i
    return max_value
