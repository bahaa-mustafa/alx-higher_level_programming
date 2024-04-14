#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    for i in range(0, 2):
        new_tuple.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(new_tuple)
    return new_tuple
