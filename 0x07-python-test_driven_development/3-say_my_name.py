#!/usr/bin/python3
"""
3-say_my_name Module

This module provides the 'say_my_name' function for formatted string
with the provided first and last names.
Usage:
    from 3-say_my_name import say_my_name
    say_my_name(first_name, last_name="")

Author:
    [ali debbache]

Date:
    [2024/01/29]
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first and last names.

    Parameters:
    - first_name (str): The first name to be included in the formatted string.
    - last_name (str, optional): The last name to be included
    in the formatted string. Default is an empty string.

    Raises:
    - TypeError: If 'first_name' or 'last_name' is not a string.

    Returns:
    - None: The function prints the formatted string
    but does not return any value.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
