#!/usr/bin/python3
"""
MyList class
class that inherits from list.
Author:
[ali debbache]
Date:
[2024/02/05]
"""

class MyList:
        """
        Prints the list in sorted (ascending) order.
        """
        def print_sorted(self):
            sorted_list = sorted(self)
            print(sorted_list)
