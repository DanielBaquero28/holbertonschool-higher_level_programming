#!/usr/bin/python3
"""
Function's name: matrix_divided()

Test command: python3 -m doctest -v ./tests/2-matrix_divided.txt

"""
def matrix_divided(matrix, div):
    """
    Divides each element by the total number of elements in each array.

    Return:
    New matrix
    """
    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for rows in matrix:
        if not rows or not isinstance(rows, list):
            raise TypeError(error)
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elements in rows:
            if isinstance(elements, (int, float)):
                elements = int(elements)
            else:
                raise TypeError(error)

    new_matrix = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)),
                          matrix))
    return (new_matrix)
