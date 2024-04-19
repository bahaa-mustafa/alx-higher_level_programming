#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    flag = 0
    my_list = sorted(my_list)
    for i in my_list:
        if i != flag:
            result += i
        flag = i
    return result
