#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Default is 98.

    Raises:
    - TypeError: If either 'a' or 'b' is not an integer or float.

    Returns:
    - int or float: The sum of 'a' and 'b'.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b
