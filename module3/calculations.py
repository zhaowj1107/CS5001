'''
File: calculations.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-6: calculations

'''

def calculations():
    '''
    Function calculations()
    Parameters: None
    Returns: None 
    '''
    number_count = int(input("Enter the number of values to read: "))
    sum = 0
    count = number_count
    while count > 0:
        number = int(input("Enter a number: "))
        sum = number + sum
        count -= 1
    print("The sum of the numbers is: ", sum)
    average = sum / number_count    
    print("The average of the numbers is: ", average)

if __name__ == "__main__":
    calculations()