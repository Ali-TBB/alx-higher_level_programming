#!/usr/bin/python3
"""
Rectangle Models.
Author:
[ali debbache]
Date:
[2024/02/11]
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Identifier of the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width or height is <= 0, or if x or y is < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.__validate_type(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.__validate_type(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x-coordinate."""
        self.__validate_type(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y-coordinate."""
        self.__validate_type(value, "y")
        self.__y = value

    def __validate_type(self, value, attribute):
        """Validate if a value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))

        if attribute in ["width", "height"]:
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        elif attribute in ["x", "y"]:
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """
        Calculate the area of the geometry object.

        Returns:
        - float: The area of the geometry object.

        Note:
        This method should be implemented in subclasses.
        """
        return self.width * self.height

    def display(self):
        """
        Display information about the geometry object.

        Returns:
        - str: A string containing information about the geometry object.

        Note:
        This method should be implemented in subclasses.
        """
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Return string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update Rectangle attributes."""
        if args:
            att = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, att[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the Rectangle object to a dictionary.

        Returns:
        - dict: A dictionary containing the attributes of the Rectangle object.
        """
        attributes = ["id", "width", "height", "x", "y"]
        dictionary = {}
        for key in attributes:
            dictionary[key] = getattr(self, key)
        return dictionary
