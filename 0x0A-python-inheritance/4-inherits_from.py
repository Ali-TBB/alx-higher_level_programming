#!/usr/bin/python3
"""
inherits_from function.
function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, False.

    Parameters:
    - obj: The object to check.
    - base_class: The specified base class.

    Returns:
    - bool: True if obj is an instance of a subclass; False otherwise.
    """
    return (issubclass(type(obj), base_class))
