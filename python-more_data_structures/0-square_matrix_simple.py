#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix2 = []
    for row in matrix:
        new_matrix = list(map(lambda value: value*value, row))
        new_matrix2.append(new_matrix)
    return new_matrix2
