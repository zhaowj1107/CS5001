"""
File: test_triangle.py
Author: Weijian Zhao(David)
Date: 2025-03-18
Class: CS_5001, Spring_2025
Description: 
homework 7: test_Shapes
"""

import pytest
from triangle import Triangle

def test_constructor():
    """
    Test the constructor
    """
    c = Triangle(5, 5, "red")
    assert c.base == 5
    assert c.height == 5
    assert c.color == "red"

def test_constructor_error():
    """
    Test the constructor with invalid input
    """
    with pytest.raises(TypeError):
        c = Triangle("red", 5)
    with pytest.raises(TypeError):
        c = Triangle(5, "red")
    with pytest.raises(TypeError):
        c = Triangle("red", "red")
    with pytest.raises(TypeError):
        c = Triangle("red", "red", "red")
    with pytest.raises(TypeError):
        c = Triangle(5, "red", "red")
    with pytest.raises(TypeError):
        c = Triangle("red", 5, "red")

def test_constructor_error2():
    """
    Test the constructor with negative input
    """
    with pytest.raises(ValueError):
        c = Triangle(-5, 5)
    with pytest.raises(ValueError):
        c = Triangle(5, -5)
    with pytest.raises(ValueError):
        c = Triangle(-5, -5)

def test_area():
    """
    Test the area method
    """
    c = Triangle(5, 5)
    assert c.area() == 12.5

def test_perimeter():
    """
    Test the perimeter method
    """
    c = Triangle(3, 4)
    assert c.perimeter() == 12.0

def test_str():
    """
    Test the str method
    """
    c = Triangle(5, 5, "red")
    assert str(c) == "Red triangle with base of 5 and height of 5"

def test_str_without_color():
    """
    Test the str method without color
    """
    c = Triangle(5, 5)
    assert str(c) == "Triangle with base of 5 and height of 5"

def test_eq():
    """
    Test the eq method
    """
    c1 = Triangle(5, 5)
    c2 = Triangle(5, 5)
    assert c1 == c2
