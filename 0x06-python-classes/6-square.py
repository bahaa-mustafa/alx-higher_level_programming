#!/usr/bin/python3
"""square class module"""


class Square:
    """define square"""
    def __init__(self, size=0, position=(0, 0)):
        """constractor.

        Args:
            size: size of side square
            position: position of two points
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Position of two points.

        Raise:
            TypeError: if not tuple of 2 position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        for c in value:
            if not isinstance(c, int) or not c >= 0:
                raise TypeError("position must be a tuple of 2 positive integers")

            if len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Area of self square.

        Return: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Print # for value of size and " " for position."""
        if self.size == 0:
            print("")
            return
        for n in range(self.__position[1]):
            print("")
        for t in range(self.size):
            i, t = 0, 0
            while t < self.__position[0]:
                print(" ", end="")
                t = t + 1
            while i < self.__size:
                print('#', end="")
                i = i + 1
            print()
