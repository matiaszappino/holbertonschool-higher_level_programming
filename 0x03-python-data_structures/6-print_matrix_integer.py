#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for c in range(len(matrix)):
            for r in range(len(matrix[c])):
                if r != len(matrix[c]) - 1:
                    print("{:d}".format(matrix[c][r]), end=" ")
                else:
                    print("{:d}".format(matrix[c][r]), end="")
            print()
