#!/usr/bin/python3
"""
load_from_json_file function
function that creates an Object from a “JSON file”.
Author:
[ali debbache]
Date:
[2024/02/06]
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    - filename (str): The path to the JSON file.

    Returns:
    - object: The Python object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
