#!/usr/bin/python3
"""ALXInterview: Rotate 2D Matrix."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise."""
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for row in transposed:
        row.reverse()
    matrix[:] = transposed
