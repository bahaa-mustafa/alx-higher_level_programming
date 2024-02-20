#!/usr/bin/python3
"""Method module that write a string"""


def write_file(filename="", text=""):
    """write a string from text to filename.
    Args:
        filename: name of file
        text: the text that will write to file

    Return: number of character in text
    """
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(text)
    return file
        
