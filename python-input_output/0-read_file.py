#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """Defines the reading function"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file)
