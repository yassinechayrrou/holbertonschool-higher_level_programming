#!/usr/bin/python3
"""
matrix_divided module.
This module contain one function matrix_divided(matrix, div).

The function divides all elements of matrix
"""


def matrix_divided(matrix, div):
    """divides matrix elements
    Returns New Matrix
    Raises TypeError and ValueError"""
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if (isinstance(div, (float, int))) is False:
        raise TypeError("div must be a number")
    if (isinstance(matrix, list)) is False:
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    for row in matrix:
        if (isinstance(row, list)) is False:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(matrix[0]) is not len(row):
            raise("Each row of the matrix must have the same size")
        for i in row:
            if (isinstance(i, (int, float))) is False:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        new_matrix = []
        for elem in matrix:
            new_matrix.append(list(map(lambda x: round((x / div), 2), elem)))
        return new_matrix
