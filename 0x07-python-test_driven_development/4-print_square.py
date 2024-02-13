#!/usr/bin/python3
"""square function module"""


def print_square(size):
    """print times size * size as #.
    Args:
        size: number of squar print
    Raise:
        TypeError: if size not int value
        ValueError: if size less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for t in range(size):
            print("#", end="")
        print()
