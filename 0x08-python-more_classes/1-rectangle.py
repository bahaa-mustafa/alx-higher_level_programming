#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        """initiale the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width instance attribute.

        Return: self.width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for width instance attribute.

        Raise:
            TypeError: if value not integer
            ValueError: if value less than 0
        """

        if not isinstance(int, value):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter of height instance attribute.

        Return: self.height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height instance attribute.

        Raise:
            TypeError: if value not integer
            ValueError: if value less than 0
        """

        if not isinstance(int, value):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
