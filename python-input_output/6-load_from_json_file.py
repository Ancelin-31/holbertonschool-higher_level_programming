#!/usr/bin/python3
"""Creates an object from a json file"""
import json


def load_from_json_file(filename):
    """Defines the reading and creating function"""
    with open(filename, 'r+', encoding="utf-8") as f:
        return json.load(f)
