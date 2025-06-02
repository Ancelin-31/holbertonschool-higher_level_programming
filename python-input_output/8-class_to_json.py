#!/usr/bin/python3
"""Returns the dictionary description with simple data structure
for JSON serialization of an object:"""


def class_to_json(obj):
    """Defines the dictionary returning function"""
    return obj.__dict__
