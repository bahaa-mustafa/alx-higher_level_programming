#!/usr/bin/python3
"""Method module that create an object from json file"""


import json


def load_from_json_file(filename):
    """create an object from json file.
    Args:
        filename: name of text file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
