#!/usr/bin/python3
"""
load_from_json_file function
function that creates an Object from a “JSON file”.
Author:
[ali debbache]
Date:
[2024/02/06]
"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the Student object to a JSON-compatible dictionary.

        Returns:
        - dict: A dictionary containing the attributes of the Student object.
        """
        return vars(self)
