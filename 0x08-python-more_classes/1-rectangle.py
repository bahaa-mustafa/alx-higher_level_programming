#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width instance attribute.

        Return: self.width
        """
        return self.width

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

        self.width = value

    @property
    def height(self):
        """getter of height instance attribute.

        Return: self.height
        """
        return self.height

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
        self.height = value
