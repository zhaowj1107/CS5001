'''
File: remove_break.py
Author:  Weijian Zhao (David)
Date: 2025-01-29
Class: CS_5001, Spring_2025
'''


def mystery_function():
    """
    Function: mystery_function
    Prints Fibonacci sequence up to 1000
    It use a while loop with condition C <= 1000
    >>> mystery_function()  # doctest: +ELLIPSIS
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    144
    233
    377
    610
    987
    1597
    """
    a = 0
    b = 1
    c = 0
    print("0\n1")
    while c <= 1000:
        c = a + b
        print(c)
        a = b
        b = c


def main():
    mystery_function()


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
