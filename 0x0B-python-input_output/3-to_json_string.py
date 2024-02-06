#!/usr/bin/python3
"""
to_json_string function
function that returns the JSON representation of an object.
Author:
[ali debbache]
Date:
[2024/02/06]
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Parameters:
    - obj: The object to be converted to JSON.

    Returns:
    - str: The JSON representation of the object.
    """
    return json.dumps(obj)
