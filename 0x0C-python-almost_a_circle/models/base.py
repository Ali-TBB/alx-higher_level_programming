#!/usr/bin/python3
"""
Base Models.
Author:
[ali debbache]
Date:
[2024/02/11]
"""
import json
import os

class Base:
    """
    Base class for creating objects with unique identifiers.

    Attributes:
        __nb_objects (int): A class attribute to track the
        number of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The unique identifier for the object.
            If not provided,
                the __nb_objects count is used to assign a new ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the inpu
            list of dictionaries.
            Returns "[]" if the input list is None.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fjson:
            if list_objs is None:
                fjson.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                fjson.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a Python object.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A Python object decoded from the JSON string.
            If the input JSON string is None, an empty list is returned.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already
        set using a dictionary.
        Args:
            **dictionary: A dictionary containing attribute names and values.
        Returns:
            Base: An instance with attributes set according
            to the provided dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of objects.
        Parameters:
        - cls (type): The class of the objects to be loaded.
        Returns:
        - list: A list containing instances of the specified
        class loaded from the JSON file.
        Note:
        The class must have a class method `create(**dictionary)`
        for instantiation.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as fjson:
            file_string = fjson.read()
            dict = Base.from_json_string(file_string)
            return [cls.create(**d) for d in dict]
