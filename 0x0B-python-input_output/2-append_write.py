#!/usr/bin/python3
"""
append_write function
function that appends a string at the end of a text file.
Author:
[ali debbache]
Date:
[2024/02/06]
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file.

    Parameters:
    - filename (str): The path to the file to be write.
    - text (str): string will be added on the end of text file.
    Returns:
    - int: The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

        return len(text)
