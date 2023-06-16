#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    new_matrix = []
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            if len(matrix) > 1:
                if len(matrix[0]) != len(matrix[1]):
                    raise TypeError("Each row of the matrix \
                                    must have the same size")
            if (type(div)) != int and (type(div)) != float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = list(map(lambda n: round(n / div, 2), row))
        new_matrix.append(new_row)
    return new_matrix
