#!/usr/bin/python3
"""
2-matrix_divided Module

This module provides the 'matrix_divided' function for Divides
all elements of a matrix by a given divisor.
Usage:
    from 2-matrix_divided import matrix_divided
    matrix_divided(matrix, div)

Author:
    [ali debbache]

Date:
    [2024/01/29]
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): The input matrix.
    - div (int or float): The divisor.

    Raises:
    - TypeError: If 'div' is not a number.
    - TypeError: If the matrix is not a list of lists of integers/floats.
    - TypeError: If each row of the matrix does not have the same size.
    - ZeroDivisionError: If 'div' is 0.

    Returns:
    - list of lists: A new matrix with elements divided by 'div'.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(row_size == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")


    new_matrix = []

    for row in matrix:
        new_row = []
        for i in row:

            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix

