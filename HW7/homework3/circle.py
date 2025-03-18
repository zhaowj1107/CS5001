"""
File: circle.py
Author: Weijian Zhao(David)
Date: 2025-03-10
Class: CS_5001, Spring_2025
Description: 
homework 7: Shapes
"""
from math import pi


class Circle():
    def __init__(self, radius, color=None):
        """
        Constructor
        :param radius: float, the radius of the circle
        :param color: str, the color of the circle
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be greater than zero")
        self.radius = radius
        self.color = color

    def area(self):
        """
        Calculate the area of the circle
        :return: float, the area of the circle
        """
        return round(pi * self.radius ** 2, 2)

    def perimeter(self):
        """
        Calculate the perimeter of the circle
        :return: float, the perimeter of the circle
        """
        return round(2 * pi * self.radius, 2)

    def __str__(self):
        """
        Return the string representation of the circle
        :return: str, the string representation of the circle
        """
        if self.color is None:
            return f"Circle with radius of {self.radius}"
        else:
            return f"{self.color.capitalize()} circle with radius of {self.radius}"

    def __eq__(self, other):
        """
        Compare the area of the circle with another circle
        :param other: Circle, the other circle
        :return: bool, True if the areas are equal, False otherwise
        """
        if isinstance(other, Circle):
            return self.area() == other.area()


if __name__ == "__main__": # pragma: no cover
    c1 = Circle(5)
    print(c1)
    print(c1.area())
    print(c1.perimeter())

    c2 = Circle(6, "red")
    print(c2)
    print(c2.area())
    print(c2.perimeter())

    c3 = Circle(5)
    print(c1 == c3)
    print(c1 == c2)
