#!/usr/bin/python3
"""
Rectangle class.
class Rectangle that inherits from BaseGeometry.
Author:
[ali debbache]
Date:
[2024/02/05]
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class"""
    def __init__(self, width, height):
        """ instantiation  function"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
