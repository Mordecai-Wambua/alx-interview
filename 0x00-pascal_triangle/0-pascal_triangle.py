#!/usr/bin/python3

"""Function to create the Pascal's triangle."""


def pascal_triangle(n):
    """
    Return a list of lists of integers.

    Args:
        n (int): size of triangle
    """
    output = []
    if n <= 0:
        return output

    for i in range(n):
        list = []

        for j in range(i+1):
            if j == 0 or j == i:
                list.append(1)
            else:
                list.append(output[i-1][j-1] + output[i-1][j])
        output.append(list)
    return output
