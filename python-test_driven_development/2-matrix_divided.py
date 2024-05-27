#!/usr/bin/python3

"""
This module divides all elements of matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): A 2D list representing the matrix.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with the /
        division results, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats,
                    or if div is not a number,
                    or if matrix rows are not of the same size.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or /
    not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix /
                (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix /
                    (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
