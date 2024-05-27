#!/usr/bin/python3

"""
This module divides all elements of matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix.

    Args:
        matrix: matrix.
        div: number to divide.

    Returns:
        New matrix.

    Raises:
        TypeError: if matrix is not a list of integers or floats.
        TypeError: if rows in matrix is not of the same size.
    """
    new_matrix = []
    for row in matrix:
        for i, element in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(element), end=' ')
            else:
                print("{:d}".format(element), end='')

    return new_matrix

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
