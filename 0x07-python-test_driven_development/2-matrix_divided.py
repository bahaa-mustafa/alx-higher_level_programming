#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """divid nmbers in matrix by div.
    Args:
        matrix: list of lists
        div: the number that divided by
    Return:
        new matrix as list
    Raise:
        TypeError: when list of lists not int or float
        TypeError: when each row of matrix not in same size
        TypeError: when div not int or float
        ZeroDivisionError: when div == 0
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
