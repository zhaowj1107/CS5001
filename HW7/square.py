"""
File: square.py
Author: Weijian Zhao(David)
Date: 2025-03-10
Class: CS_5001, Spring_2025
Description: 
homework 7: Shapes
"""


class Square():
    def __init__(self, length, color=None):
        """
        Constructor
        :param length: float, the length of the square
        :param color: str, the color of the square
        """
        if not isinstance(length, (int, float)):
            raise TypeError("length must be a number")
        if length <= 0:
            raise ValueError("length must be greater than zero")
        self.length = length
        self.color = color

    def area(self):
        """
        Calculate the area of the square
        :return: float, the area of the square
        """
        return self.length ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the square
        :return: float, the perimeter of the square
        """
        return 4 * self.length

    def __str__(self):
        """
        Return the string representation of the square
        :return: str, the string representation of the square
        """
        if self.color is None:
            return f"Square with length of {self.length}"
        else:
            return f"{self.color.capitalize()} square with length of {self.length}"

    def __eq__(self, other):
        """
        Compare the area of the square with another square
        :param other: Square, the other square
        :return: bool, True if the areas are equal, False otherwise
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False


if __name__ == "__main__":
    c1 = Square(5)
    print(c1)
    print(c1.area())
    print(c1.perimeter())

    c2 = Square(6, "red")
    print(c2)
    print(c2.area())
    print(c2.perimeter())

    c3 = Square(5)
    print(c1 == c3)
    print(c1 == c2)
