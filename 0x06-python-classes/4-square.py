#!/usr/bin/python3
"""Square module"""


class Square:
    """define square class"""
    def __init__(self, size=0):
        """constractor.

        Args:
            size: value of side square
       """

    def area(self):
        """Area of self squar.

        Return: area of squar.
        """
        return self.__size * 2

    @property
    def size(self):
        """define getter method.

        Return: self size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """define setter method.

        Args:
            value: value os size to check and set

        Raises:
            TypeError: when size isn't int
            ValueError: size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value