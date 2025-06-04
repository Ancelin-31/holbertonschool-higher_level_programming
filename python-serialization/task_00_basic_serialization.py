#!/usr/bin/python3
"""Serializes and deserializes data from a filename"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(data, f))


def load_and_deserialize(filename):
    with open(filename, 'r+', encoding="utf-8") as f:
        return json.load(f)
