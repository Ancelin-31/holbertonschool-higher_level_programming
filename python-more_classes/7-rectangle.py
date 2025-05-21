#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

    def area(self):
        """Defines the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Defines the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

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
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Returns the representation of the rectangle with #."""
        if self.width == 0 or self.height == 0:
            return ""
        str_rectangle = ""
        for i in range(self.height):
            str_rectangle += str(self.print_symbol) * self.width
            if i != self.height - 1:
                str_rectangle += "\n"
        return str_rectangle

    def __repr__(self):
        """Returns a string representation."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when a resctangle instance is deleled"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
