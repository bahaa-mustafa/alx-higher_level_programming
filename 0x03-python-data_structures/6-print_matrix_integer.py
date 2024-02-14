#!/usr/bin/python3
"""function module"""


def print_matrix_integer(matrix=[[]]):
    """print a matrix of integers"""
    if not matrix:
        return None
    for i in matrix:
        if len(i) == 0:
            print()
        for t in range(len(i)):
            print("{:d}".format(i[t]), end='\n' if t == (len(i) - 1) else " ")
