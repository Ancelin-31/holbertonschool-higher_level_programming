#!/usr/bin/python3
"""Writes an object in a text file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Defines the writing function"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
