#!/usr/bin/python3
"""Method model read and write"""


def read_file(filename=""):
    """read date from file and print it.
    Args:
        filename: name of file
    """
    with open(filename, encoding="UTF8") as file:
        print(file.read(), end="")

