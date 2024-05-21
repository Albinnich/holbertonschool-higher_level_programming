#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:i}{:i}".format(i, j), end=' ')
        print()
