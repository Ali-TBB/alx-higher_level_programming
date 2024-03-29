#!/usr/bin/python3
"""
Rectangle class.
class Rectangle that inherits from BaseGeometry.
Author:
[ali debbache]
Date:
[2024/02/05]
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size):
        """ instantiation  function"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
