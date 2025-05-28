#!/usr/bin/python3
"""Create an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        if not width:
            raise AttributeError("'Rectangle'object has no attribute {}".format(width))
        if not height:
            raise AttributeError("'Rectangle'object has no attribute {}".format(height))
