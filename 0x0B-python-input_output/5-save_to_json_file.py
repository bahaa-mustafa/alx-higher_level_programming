#!/usr/bin/python3
"""Method module write object to file"""


import json


def save_to_json_file(my_obj, filename):
    """confert data structure to json and write it to file.
    Args:
        my_obj: data structure
        filename: name of text file
    """
    my_str = json.dumps(my_obj)
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(my_str)
