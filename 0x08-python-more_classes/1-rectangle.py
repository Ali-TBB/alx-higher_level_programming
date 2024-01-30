#!/usr/bin/python3
"""
Rectangle Class

This is defined of rectangle class.

Author:
[ali debbache]

Date:
[2024/01/30]
"""


class Rectangle:
    """the Rectangle class."""
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width


    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height


    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
