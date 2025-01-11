'''
File: nest.py
Author: Weijian Zhao (David)
Date: 2025-01-07
Class: CS_5001, Spring_2025
Description:
Enter your description here
'''

def main():
    number = int(input("Enter a number between 1 and 100: "))
    if number >= 1:
        if number <= 100:
            print("in range")
        else:
            print("The number is too high.")
    else:
        print("The number is too low.")

main()
