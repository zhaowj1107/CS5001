'''
File: count_up.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-1: Count up

'''

def count_up(x):
    '''
    Function count_up()
    Parameters: None
    Returns: None
    >>> count_up(5)
    1
    2
    3
    4
    5
    >>> count_up(1)
    1
    >>> count_up(0)
    '''
    counter = 1
    while counter <= x:
        print(counter)
        counter += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    count_up(5)