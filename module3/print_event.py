'''
File: print_event.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-1: print event

'''

def print_event():
    '''
    Function print_event()
    Parameters: None
    Returns: None
    '''
    counter = 100
    while counter > 1:
        print(counter)
        counter -= 2

if __name__ == "__main__":
    print_event()