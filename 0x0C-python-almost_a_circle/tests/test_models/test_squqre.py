#!/usr/bin/python3
"""
test_square Models.
Author:
[ali debbache]
Date:
[2024/02/12]
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Unit tests for the Square class methods.
    """

    def test_init(self):
        """
        Test the initialization of the Square class.
        """
        # Test with valid arguments
        square = Square(5, 1, 2, 123)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 123)

        # Test with invalid arguments
        with self.assertRaises(TypeError):
            Square("invalid", 1, 2, 123)
        with self.assertRaises(ValueError):
            Square(-5, 1, 2, 123)

    def test_str(self):
        """
        Test the string representation of the Square class.
        """
        square = Square(5, 1, 2, 123)
        self.assertEqual(str(square), "[Square] (123) 1/2 - 5")

    # Add similar tests for other methods like update,
    # to_dictionary, etc.


if __name__ == '__main__':
    unittest.main()
