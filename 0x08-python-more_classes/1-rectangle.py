#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        """initiale the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width instance attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter of height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height instance attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
