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

    def integer_validator(self, name, value):
        """
        Raises an Exception with if typeerror or valueerror'.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
