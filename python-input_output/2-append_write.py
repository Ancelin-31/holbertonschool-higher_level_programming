#!/usr/bin/python3
"""Appends text into a file"""


def append_write(filename="", text=""):
    """Defines the appending function"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
