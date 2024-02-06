#!/usr/bin/python3
"""
write_file function
function that writes a string to a text file.
Author:
[ali debbache]
Date:
[2024/02/06]
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file.

    Parameters:
    - filename (str): The path to the file to be write.
    - text (str): string will be writed on text file.
    Returns:
    - int: The number of characters writed
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

        return len(text)
