#!/usr/bin/python3
"""
is_same_class function.
function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return isinstance(obj, a_class)
