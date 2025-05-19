#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defines an area method."""
        return self.__size * self.__size

    @property
    def size(self):
        """gets the private value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets a new value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
