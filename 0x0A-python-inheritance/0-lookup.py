#!/usr/bin/python3
"""
lookup function
return the list of available attributes and methods of an object.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Parameters:
    - obj: Any Python object.
    Returns:
    - list: A list of attributes and methods.
    """

    return dir(obj)
