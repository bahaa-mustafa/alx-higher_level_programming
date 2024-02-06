#!/usr/bin/python3
"""square class module"""


class Square:
    """define square"""
    def __init__(self, size=0):
        """constractor.

        Args:
            size: size of side square
        """
        self.__size = size

    @property
    def size(self):
        """property of side of self square.

        Raise:
            TypeError: when size in not integer
            ValueError: in case size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of self square.

        Return: area of square
        """
        return self.__size ** 2
