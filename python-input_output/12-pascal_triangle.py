#!/usr/bin/python3

"""
The ''12. Pascal's Triangle'' module
"""


def pascal_triangle(n):
    """
    pascal_triangle function returns list of lists integers
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
