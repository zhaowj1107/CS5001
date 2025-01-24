'''
File: non_negative.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-4: non_negative

'''

def non_negative():
    '''
    Function non_negative()
    Parameters: None
    Returns: None
    '''
    while True:
        number = int(input("Enter a number: "))
        if number >= 0:
            print(number)
            return number
        else:
            break

if __name__ == "__main__":
    non_negative()