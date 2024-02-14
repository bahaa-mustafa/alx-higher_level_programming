#!/usr/bin/python3
"""function module"""


def new_in_list(my_list, idx, element):
    """return new list after replace element in index"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
