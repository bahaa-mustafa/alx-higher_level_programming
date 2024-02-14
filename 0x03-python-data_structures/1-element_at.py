#!/usr/bin/python3
"""function module"""


def element_at(my_list, idx):
    """return element at index idx"""
    if idx < 0:
        return None
    if len(my_list) > idx:
        return (my_list[idx])
    return None
