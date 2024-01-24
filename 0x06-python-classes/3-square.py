#!/usr/bin/python3
"""Square class take size as private attribute"""
class Square:
    """This class represents a square with a private attribute 'size'."""
    def __init__(self, size=0):
        self.__size = None
        self.set_size(size)

    def set_size(self, new_size):
        """Setter method for the 'size' attribute."""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
