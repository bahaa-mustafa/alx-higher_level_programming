#!/usr/bin/python3
"""Square module"""


class Square:
    """define square class"""
    def __init__(self, size=0):
        """constractor.

        Args:
            size: value of side square

        Raises:
            TypeError: when size isn't int
            ValueError: size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Area of self squar.

        Return: area of squar.
        """
        return self.__size * 2
