'''
File: count_down.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-2: Count down

'''

def count_down(x):
    '''
    Function count_down()
    Parameters: None
    Returns: None
    >>> count_down(5)
    5
    4
    3
    2
    1
    >>> count_down(1)
    1
    >>> count_down(0)
    '''
    while x>=1:
        print(x)
        x -= 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    count_down(5)
