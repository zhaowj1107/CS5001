"""
File: shapes_driver.py
Author: Weijian Zhao(David)
Date: 2025-02-24
Class: CS_5001, Spring_2025
Description: 
homework 1:Shapes
"""
from triangle import Triangle
from square import Square
from circle import Circle


def main():
    """
    The main function
    :return: None
    """
    # Create a circle with radius 5 and color red
    c = Circle(5, "red")
    print(c)
    print(f"The area of the circle is {c.area():.2f}")
    print(f"The circumference of the circle is {c.perimeter():.2f}")

    # Create a triangle with base 5, height 10 and color green
    t = Triangle(5, 10, "green")
    print(t)
    print(f"The area of the triangle is {t.area():.2f}")
    print(f"The perimeter of the triangle is {t.perimeter():.2f}")

    # Create a square with length 5 and color yellow
    s = Square(5, "yellow")
    print(s)
    print(f"The area of the square is {s.area():.2f}")
    print(f"The perimeter of the square is {s.perimeter():.2f}")


if __name__ == "__main__":
    main()
