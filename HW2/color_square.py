'''
File: chessboard.py
Author: Weijian Zhao (David)
Date: 2025-01-20
Class: CS_5001, Spring_2025
Description: 
homework 2-1: chessboard

'''

import chessboard as cb


def main():
    """
    Function main()
    Parameters: none
    Returns: None
    """
    print("Please input a chess square to check tis color:")
    row = input("what is the row (1-8)? ")
    column = input("what is the column (A-H)? ")
    if cb.check_valid_row(row):
        if cb.check_valid_column(column):
            color = cb.determine_black_or_white(int(row), column)
            cell = column + str(row)
            print(f"The square {cell} is {color}.")
        else:
            print("Encountered the following errors with your inputs:")
            print("Invalid column imput. it must be a letter between A & H")
    else:
        print("Encountered the following errors with your inputs:")
        print("Invalid row imput. it must be a letter between 1 & 8")


if __name__ == "__main__":
    main()
