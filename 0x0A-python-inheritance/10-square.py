#!/usr/bin/python3
"""
Rectangle class.
class Rectangle that inherits from BaseGeometry.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size):
        """ instantiation  function"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """returns the area of the square"""
        return size ** 2
