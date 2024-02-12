#!/usr/bin/python3
"""
test_base Models.
Author:
[ali debbache]
Date:
[2024/02/12]
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unit tests for the Base class methods.
    """

    def test_to_json_string(self):
        """
        Test the to_json_string method of the Base class.
        """
        # Test when list is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when list is not empty
        test_list = [{'key': 'value'}, {'key2': 'value2'}]
        expected_json_string = '[{"key": "value"}, {"key2": "value2"}]'
        self.assertEqual(Base.to_json_string(test_list), expected_json_string)

    def test_from_json_string(self):
        """
        Test the from_json_string method of the Base class.
        """
        # Test when JSON string is None
        self.assertEqual(Base.from_json_string(None), [])

        # Test when JSON string is not None
        json_string = '[{"key": "value"}, {"key2": "value2"}]'
        expected_list = [{'key': 'value'}, {'key2': 'value2'}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    # Add similar tests for other methods like save_to_file,
    # load_from_file, create, etc.


if __name__ == '__main__':
    unittest.main()
