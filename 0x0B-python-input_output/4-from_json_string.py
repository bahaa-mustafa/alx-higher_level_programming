#!/usr/bin/python3
"""Method module reserialization json object"""


import json


def from_json_string(my_str):
    """reserialization of json object to data structure.
    Args:
        my_str: json object
    Return: data structure
    """
    return json.loads(my_str)
