#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    if len(my_list) == 0:
        return None
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
