#!/usr/bin/python3
"""Method module"""


def is_same_class(obj, a_class):
    """check if obj and a_class same tybe
    Args:
        obj: our object
        a_class: atype
    Return: true in right and false in other
    """
    if type(obj) == type(a_class):
        return True
    return False
