#!/usr/bin/python3
"""
4-print_square Module

This module provides the 'print_square' function for printing a square 
of a given size.
Usage:
    from 4-print_square import print_square
    print_square(size)

Author:
    [ali debbache]

Date:
    [2024/01/29]
"""
def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    - size (int): The size of square.

    Raises:
    - TypeError: If 'size' is not a integer.
    - ValueError: If 'size' is less than 0.

    Returns:
    - None: The function prints the square  but does not return any value.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")


    if size < 0:
        raise ValueError("size must be >= 0")


    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
