#!/usr/bin/python3
"""
load_from_json_file function
function that creates an Object from a “JSON file”.
Author:
[ali debbache]
Date:
[2024/02/06]
"""


def class_to_json(obj):
    """
    Converts an object to a dictionary representation.

    Parameters:
    - obj (object): The object to convert.

    Returns:
    - dict: A dictionary representation of the object's attributes and their values.
    """
    return vars(obj)
