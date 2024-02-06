#!/usr/bin/python3
"""
from_json_string function
function that returns an object (Python data structure)
represented by a JSON string.
Author:
[ali debbache]
Date:
[2024/02/06]
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Parameters:
    - my_str: The object to be converted to JSON.

    Returns:
    - object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
