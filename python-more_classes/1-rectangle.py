#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the private width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle to a new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the private height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle to a new value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
