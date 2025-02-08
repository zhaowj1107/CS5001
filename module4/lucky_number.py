"""
File: count_down.py
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
Module 4: lucky_number
"""

def number_checker(number, digit = 0):
    """
    function: number_checker
    input: number: str
    """
    while number > 0:
        if number % 10 == digit:
            return True
        else:
            number, per_digit = number // 10, number % 10
    return False

def main():
    """
    function: number_checker
    input: number: str
    """
    LUCKY_NUMBER = 8
    list_number = list(range(1,101))
    result_list = []
    for number in range(1,101):
        if number_checker(number, LUCKY_NUMBER):
            result_list.append(number)
            list_number[number] = "\U0001F40D"

    print(list_number)
    return result_list
    
        
if __name__ =="__main__":
    main()