#!/usr/bin/python3
"""
test_rectangle Models.
Author:
[ali debbache]
Date:
[2024/02/12]
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class methods.
    """

    def test_init(self):
        """
        Test the initialization of the Rectangle class.
        """
        # Test with valid arguments
        rect = Rectangle(5, 10, 1, 2, 123)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 123)

        # Test with invalid arguments
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 1, 2, 123)
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 1, 2, 123)

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    # Add similar tests for other methods like display,
    # update, to_dictionary, etc.


if __name__ == '__main__':
    unittest.main()
