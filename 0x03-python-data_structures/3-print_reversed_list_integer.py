#!/usr/bin/python3
"""function module"""


def print_reversed_list_integer(my_list=[]):
    """print list in reverse way"""
    if not my_list:
        return None
    my_list = reversed(my_list)
    for i in my_list:
        print("{:d}".format(i))
