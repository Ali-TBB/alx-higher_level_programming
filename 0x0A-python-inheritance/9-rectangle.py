#!/usr/bin/python3
"""
Rectangle class.
class Rectangle that inherits from BaseGeometry.
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
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class"""
    def __init__(self, width, height):
        """ instantiation  function"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
