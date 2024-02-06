#!/usr/bin/python3
"""
save_to_json_file function
function that writes an Object to a text file,
using a JSON representation.
Author:
[ali debbache]
Date:
[2024/02/06]
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Parameters:
    - filename (str): The path to the file to be write.
    - my_obj: The object to be converted to JSON.

    Returns:
    - None.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
