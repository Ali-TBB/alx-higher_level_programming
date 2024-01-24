#!/usr/bin/python3
"""Square class take size as private attribute"""
class Square:
    """This class represents a square with a private attribute 'size'."""
    def __init__(self, size=0):
        # Private instance attribute
        self.__size = None
        self.size(size)
    def size(self):
        """Getter method for the 'size' attribute."""
        return self.__size
    def size(self, value):
        """Setter method for the 'size' attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
