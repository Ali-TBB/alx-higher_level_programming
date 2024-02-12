#!/usr/bin/python3
"""
Square Models.
Author:
[ali debbache]
Date:
[2024/02/11]
"""


from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Rectangle."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
            )

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.__validate_type(value, "size")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """Update Rectangle attributes."""
        if args:
            att = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if att[i] == "size":
                    setattr(self, "width", arg)
                    setattr(self, "width", arg)
                else:
                    setattr(self, att[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the Square object to a dictionary.

        Returns:
        - dict: A dictionary containing the attributes of the Rectangle object.
        """
        attributes = ["id", "size", "x", "y"]
        dictionary = {}
        for key in attributes:
            dictionary[key] = getattr(self, key)
        return dictionary
