#!/usr/bin/python3

""" matrix_divided
Divides a matrix with a specified value
"""


def matrix_divided(matrix, div):
    """ function divides a matrix with specified value

    args:
        matrix: list of list of int or float
        div: value to be used as divisor

    Returns: a new matrix on success

    Raises:
        TypeError: if matrix is not int or float and row length is unequal
        ZeroDivisionError: if div is zero
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Checks if matrix is a list
    if isinstance(matrix, list):
        res = True

    # Raise error if parameter is not matrix
    if res is False:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # check if list is empty
    if not matrix:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # check if all elements in the lists are lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Check if all rows have the same length
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # Check if all elements in matrix are integers or floats
    if not all(isinstance(value, (int, float)) for row in matrix for value in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Divide each element by div and return new matrix
    # Round off to 2decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(value / div, 2) for value in row]
        new_matrix.append(new_row)

    return new_matrix
