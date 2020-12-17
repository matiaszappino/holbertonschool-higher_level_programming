#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []
    new_matrix.append(list(map(lambda x:(map(lambda j: j**2, matrix)))))
    return new_matrix
