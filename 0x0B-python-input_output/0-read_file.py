#!/usr/bin/python3
"""
read_file function
function that reads a text file.
Author:
[ali debbache]
Date:
[2024/02/06]
"""


def read_file(filename=""):
    """
    Reads and prints the content of the specified file.

    Parameters:
    - filename (str): The path to the file to be read.

    Returns:
    - None
    """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content)
