'''
File: multiples.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-6: multiples

'''

def multiples():
    '''
    Function multiples()
    Parameters: None
    Returns: None
    '''
    number_one = int(input("Enter a non-zero number: "))
    multiple_number = int(input("Enter a number to check if it is a multiple of the first number: "))   
    while multiple_number % number_one != 0:
        multiple_number = int(input("Try again: "))


if __name__ == "__main__":
    multiples()