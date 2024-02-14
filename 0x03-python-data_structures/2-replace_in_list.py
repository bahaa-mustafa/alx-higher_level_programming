#!/usr/bin/python3
"""function module"""


def replace_in_list(my_list, idx, element):
    """replace element in list"""
    if idx < 0 or len(my_list) >= idx:
        return my_list
    my_list[idx] = element
