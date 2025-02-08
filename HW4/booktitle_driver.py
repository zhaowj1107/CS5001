"""
File: booktitle_driver
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
homework 4-1: Recipe Ingredient Scrubber
"""
import booktitle as bt


def main():
    """
    Function main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    user_input = input("Enter the  title: ")
    if bt.validate_booktitle(user_input):
        print("Valid title")
    else:
        print("Invalid title")


if __name__ == "__main__":
    main()
