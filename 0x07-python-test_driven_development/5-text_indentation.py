#!/usr/bin/python3
"""
5-text_indentation Module

This module provides the 'text_indentation' function for Prints the given 
text with indentation, breaking lines after '?', '.', and ':' characters.
Usage:
    from 5-text_indentation import text_indentation
    text_indentation(text)

Author:
    [ali debbache]

Date:
    [2024/01/29]
"""
def text_indentation(text):
    """
    Prints the given text with indentation, breaking lines after '?', '.', and ':' characters.

    Parameters:
    - text (str): The input text to be formatted.

    Raises:
    - TypeError: If 'text' is not a string.

    Returns:
    - None: The function prints the formatted text but does not return any value.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_space = False
    for char in text:
        if char in ['?', '.', ':']:
            print(char)
            print()
            skip_space = True
        elif char == ' ' and skip_space:
            continue
        else:
            print(char, end="")
            skip_space = False
