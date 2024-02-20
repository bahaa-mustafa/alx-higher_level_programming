#!/usr/bin/python3
"""Method module to create json object"""


import json


def to_json_string(my_obj):
    """create json object.
    Args:
        my_obj: object that will serialization
    Return: JSON object
    """
    return json.dumps(my_obj)
