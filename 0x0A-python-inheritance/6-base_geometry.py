#!/usr/bin/python3
"""
BaseGeometry class.
class that Raises an Exception with the message
'area() is not implemented'.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


class BaseGeometry:
    """ BaseGeometry class"""
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
