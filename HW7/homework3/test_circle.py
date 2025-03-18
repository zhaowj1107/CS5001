"""
File: test_circle.py
Author: Weijian Zhao(David)
Date: 2025-03-18
Class: CS_5001, Spring_2025
Description: 
homework 7: test_Shapes
"""

import unittest
from circle import Circle

class TestCircle(unittest.TestCase):
    def test_constructor(self):
        """
        Test the constructor
        """
        c = Circle(5, "red")
        self.assertEqual(c.radius, 5)
    
    def test_constructor_error(self):
        """
        Test the constructor with invalid input
        """
        with self.assertRaises(TypeError):
            c = Circle("red")
    
    def test_constructor_error2(self):
        """
        Test the constructor with invalid input
        """
        with self.assertRaises(ValueError):
            c = Circle(-5)
    
    def test_area(self):
        """
        Test the area method
        """
        c = Circle(5)
        self.assertEqual(c.area(), 78.54)
    
    def test_perimeter(self):
        """
        Test the perimeter method
        """
        c = Circle(5)
        self.assertEqual(c.perimeter(), 31.42)
    
    def test_str_without_color(self):
        """
        Test the str method without color
        """
        c = Circle(5)
        self.assertEqual(str(c), "Circle with radius of 5")

    def test_str(self):
        """
        Test the str method
        """
        c = Circle(5, "red")
        self.assertEqual(str(c), "Red circle with radius of 5")
    
    def test_eq(self):
        """
        Test the eq method
        """
        c1 = Circle(5)
        c2 = Circle(5)
        self.assertTrue(c1 == c2)

    def test_eq_false(self):
        """
        Test the eq method return False
        """
        c1 = Circle(5)
        c2 = Circle(6)
        self.assertFalse(c1 == c2)

if __name__ == "__main__": # pragma: no cover
    unittest.main()