#!/usr/bin/python3
"""Creates a class Student"""
import json

to_json = __import__('8-class_to_json').class_to_json

class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        if not isinstance(self.first_name, str):
            raise TypeError('first_name must be a string')
        if not isinstance(self.last_name, str):
            raise TypeError('last_name must be a string')
        if not isinstance(self.age, int):
            raise TypeError('age must be an int')
        if self.age <= 0:
            raise ValueError('age must be more than zero')

    def to_json(self):
        return to_json(self)
