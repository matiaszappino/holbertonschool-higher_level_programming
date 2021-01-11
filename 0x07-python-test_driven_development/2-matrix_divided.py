#!/usr/bin/python3
"""Test Module"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()


def matrix_divided(matrix, div):
    """Matrix Divided"""
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    largo = len(matrix[0])
    
    if largo == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    for elem in matrix:
        if type(elem) != list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if largo != len(elem):
            raise TypeError('Each row of the matrix must have the same size')
        for value in elem:
            if type(value) != int and type(value) != float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    new_matrix = []

    for elem in range(len(matrix)):
        new_matrix.append([])
        for value in matrix[elem]:
            new_matrix[elem].append(round((value / div), 2))
    
    return new_matrix