#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(0, len(tuple_a)):
        new_tuple.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(new_tuple)
    return new_tuple
