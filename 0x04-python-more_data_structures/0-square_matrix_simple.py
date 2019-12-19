#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rmat = [[row[i] for row in matrix] for i in range(len(matrix))]
    rmat = [[row[i]**2 for row in rmat] for i in range(len(rmat))]
    return rmat
