#!/usr/bin/python3
"""function module"""


def lookup(obj):
    """ function that returns the list of available attributes and
    ethods of an object.
    Args:
        obj: class object
    Return:
        available attributes
   """
    return dir(obj)
