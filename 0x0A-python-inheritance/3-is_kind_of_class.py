#!/usr/bin/python3
"""Method module"""


def is_kind_of_class(obj, a_class):
    """check obj is instance of class or inherited class"""
    if type(obj) == type(a_class) or isinstance(obj, object):
        return True
    return False
