#!/usr/bin/env python3
"""function module"""


def no_c(my_string):
    """return new list after remove c and C character"""
    if not my_string:
        return None
    new_string = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            new_string += my_string[i]
    return new_string
