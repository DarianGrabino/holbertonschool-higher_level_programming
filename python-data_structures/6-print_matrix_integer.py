#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in row:
            print("{:d}".format(value), end="")
            if row[-1] != value:
                print(" ", end="")
        print()
