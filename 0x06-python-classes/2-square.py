#!/usr/bin/python3
"""square class module"""


class Square:
    """define square class"""
    def __init__(self, size=0):
        """constructor.

        Args:
            size: value of side to square

        Raises:
            TypeError: when size is not int
            ValueError: when size is less than 0
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
