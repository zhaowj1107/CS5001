'''
File: words_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-12
Class: CS_5001, Spring_2025
'''


def sum_values(list_int: list, index: int):
    '''
    Recursively sums values in a list from given index to end.
    Args:
        list_int (list): List of integers to sum
        index (int): Starting index for summation
    Returns:
        int: Sum of values from index to end of list
    >>> sum_values([1, 2, 3], 0)  # Test normal case
    6
    >>> sum_values([5], 0)  # Test single element
    5
    >>> sum_values([], 0)  # Test empty list
    0
    >>> sum_values([1, -3, 2, -4, 5], 3)  # Test empty list
    1
    '''
    if not list_int:  # Handle empty list case
        return 0
    if index == len(list_int) - 1:
        return list_int[index]
    else:
        return sum_values(list_int, index + 1) + list_int[index]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
