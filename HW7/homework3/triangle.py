"""
File: triangle.py
Author: Weijian Zhao(David)
Date: 2025-02-24
Class: CS_5001, Spring_2025
Description: 
homework 1:Shapes
""" 


class Triangle():
    def __init__(self, base, height, color=None):
        """
        Constructor
        :param height: float, the height of the triangle
        :param color: str, the color of the triangle
        """
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if height <= 0:
            raise ValueError("height must be greater than zero")
        if not isinstance(base, (int, float)):
            raise TypeError("base must be a number")
        if base <= 0:
            raise ValueError("base must be greater than zero")
        self.base = base
        self.height = height
        self.color = color

    def area(self):
        """
        Calculate the area of the triangle
        :return: float, the area of the triangle
        """
        return self.base * self.height / 2

    def perimeter(self):
        """
        Calculate the perimeter of the right triangle
        :return: float, the perimeter of the triangle
        """
        return self.base + self.height + (self.base ** 2 + self.height ** 2) ** 0.5

    def __str__(self):
        """
        Return the string representation of the triangle
        :return: str, the string representation of the triangle
        """
        if self.color is None:
            return f"Triangle with base of {self.base} and height of {self.height}"
        else:
            return f"{self.color.capitalize()} triangle with base of {self.base} and height of {self.height}"

    def __eq__(self, other):
        """
        Compare the area of the triangle with another triangle
        :param other: triangle, the other triangle
        :return: bool, True if the areas are equal, False otherwise
        """
        if isinstance(other, Triangle):
            return self.area() == other.area()


if __name__ == "__main__": # pragma: no cover
    t = Triangle(3, 4, "red")
    print(t.area())
    print(t.perimeter())
    print(t.__str__())
    print(t.__eq__(t))
    t2 = Triangle(3, 4, "red")
    print(t.__eq__(t2))
