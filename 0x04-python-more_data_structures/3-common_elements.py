#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        for t in set_2:
            if i == t:
                new_set.append(i)
    return new_set
