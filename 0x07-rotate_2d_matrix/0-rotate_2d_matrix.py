#!/usr/bin/python3

""" 2D Matrix 90 Degrees Clockwise Rotation"""


def rotate_2d_matrix(matrix):
    """ Functiion for rotating 2D Matrix 90 degrees clockwise

    Given an n x n 2D matrix, rotate it 90 degrees clockwise

    - Don't returns anything. The matrix edited in-place
    - Assummed matrix will have 2 dimensions and will not be empty.
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
