#!/usr/bin/python3
"""
MyList class
class that inherits from list.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
