#!/usr/bin/python3
"""Method module that append string"""


def append_write(filename="", text=""):
    """append text to file.
    Args:
        filename: name of file
        text: text that will append
    Return: appended text
    """
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)
