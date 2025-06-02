#!/usr/bin/python3
"""Returns the JavaScript Object Notification of a file"""
import json


def to_json_string(my_obj):
    """Defines the JSON returning function"""
    return json.dumps(my_obj)
