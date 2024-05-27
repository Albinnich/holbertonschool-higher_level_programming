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

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row)
        new_matrix.append(new_row)

    return new_matrix
