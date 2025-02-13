'''
File: words_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-12
Class: CS_5001, Spring_2025
'''


def formula(x):
    '''
    Recursively calculates a value based on the formula:
    - Base case: returns 3 when x <= 1
    - Recursive case: returns 5 + 2 * formula(x - 1) when x > 1
    >>> formula(0)  # Test base case with 0
    3
    >>> formula(1)  # Test base case with 1
    3
    >>> formula(2)  # Test recursive case
    11
    >>> formula(3)  # Test deeper recursion
    27
    >>> formula(-5)  # Test negative input (edge case)
    3
    '''

    if x <= 1:
        return 3
    else:
        return 5 + 2 * formula(x - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
