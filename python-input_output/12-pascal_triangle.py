#!/usr/bin/python3
"""Technical interview preparation"""


def pascal_triangle(n):
    """create pascal triangle"""
    triangulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        triangulo.append(fila)
    return triangulo
