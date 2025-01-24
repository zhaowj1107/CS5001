'''
File: chessboard.py
Author: Weijian Zhao (David)
Date: 2025-01-20
Class: CS_5001, Spring_2025
Description: 
homework 2-1: chessboard
'''


def determine_black_or_white(row, column):
    """
    Function determine_black_or_white()
    Parameters: row, column
    Returns: string “Black” or “White”
    >>> determine_black_or_white(1,"E")
    'Black'
    >>> determine_black_or_white(7,"g")
    'Black'
    >>> determine_black_or_white(6,"c")
    'White'
    """
    capital_letter = (column == 'A' or column == 'C') or \
                     (column == 'E' or column == 'G')
    lowercase_letter = (column == 'a' or column == 'c') or \
                       (column == 'e' or column == 'g')
    if row % 2 == 0:
        if capital_letter or lowercase_letter:
            return "White"
        else:
            return "Black"
    else:
        if capital_letter or lowercase_letter:
            return "Black"
        else:
            return "White"


def check_valid_row(row):
    """
    Function check_valid_row()
    Parameters: row
    Returns: True or False
    >>> check_valid_row(1)
    True
    >>> check_valid_row(8)
    True
    >>> check_valid_row(0)
    False
    >>> check_valid_row(9)
    False
    """
    row = int(row)
    if row >= 1 and row <= 8:
        return True
    else:
        return False


def check_valid_column(column):
    """
    Function check_valid_row()
    Parameters: column
    Returns: True or False
    >>> check_valid_column('A')
    True
    >>> check_valid_column('H')
    True
    >>> check_valid_column('a')
    True
    >>> check_valid_column('h')
    True
    >>> check_valid_column('I')
    False
    >>> check_valid_column('i')
    False
    """
    column = str(column)
    column = column.upper()
    if (column >= 'A' and column <= 'H') or (column >= 'a' and column <= 'h'):
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
