#!/usr/bin/python3

def max_integer(my_list=[]):
    max = None
    if len(my_list) == 0:
        return None
    for i in range(0, len(my_list)):
        if max is None:
            max = my_list[i]
        if my_list[i] > max:
            max = my_list[i]
    return max
