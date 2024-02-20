#!/usr/bin/python3
"""Method module that create an object from json file"""


import json


def load_from_json_file(filename):
    """create an object from json file.
    Args:
        filename: name of text file
    """
    my_obj = json.loads(filename)

    with open(filename, 'w', encoding="utf-8"):
        file.write(my_obj)
