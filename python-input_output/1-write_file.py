#!/usr/bin/python3
"""Writes a file"""


def write_file(filename="", text=""):
    """Defines the writing function"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
