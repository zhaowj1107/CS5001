'''
File: atm.py
Author: Weijian Zhao (David)
Date: 2025-01-13
Class: CS_5001, Spring_2025
Description: 
homework 1-1: ATM
An Automated Teller Machine (ATM) machine. 

Test case #1:
Input: $0
Output: 0 fifties, 0 twenties, 0 tens, 0 fives, 0 toonies, 0 loonie

Test case #2:
Input: 148
Output: 2 fifties, 2 twenties, 0 tens, 1 fives, 1 toonies, 1 loonies

Test case #3:
Input: 123456789
Output: 2469135 fifties, 1 twenties, 1 tens, 1 fives, 2 toonies, 0 loonies
'''


def output(balance=0, fifties=0, twenties=0, tens=0, 
           fives=0, toonies=0, loonies=0):
    # output the result
    print("Cha-ching!")
    print(f"You asked for {balance}:")
    print("That breaks down to: ")
    print(f"{fifties} fifties")
    print(f"{twenties} twenties")
    print(f"{tens} tens")
    print(f"{fives} fives")
    print(f"{toonies} toonies")
    print(f"{loonies} loonies")


def main():
    # calculate the number of each type of currency

    balance = int(input("Welcome to NUBC Bank! How much to withdraw? ")) 
    if balance % 50 != 0:
        fifties = balance // 50
        after_balance = balance % 50
        if after_balance % 20 != 0:
            twenties = after_balance // 20
            after_balance = after_balance % 20
            if after_balance % 10 != 0:
                tens = after_balance // 10
                after_balance = after_balance % 10
                if after_balance % 5 != 0:
                    fives = after_balance // 5
                    after_balance = after_balance % 5
                    if after_balance % 2 != 0:
                        toonies = after_balance // 2
                        after_balance = after_balance % 2
                        output(balance, fifties, twenties, 
                               tens, fives, toonies, 1)
                    else:
                        toonies = after_balance // 2
                        output(balance, fifties, twenties, 
                               tens, fives, toonies)
                else:
                    fives = after_balance // 5
                    output(balance, fifties, twenties, tens, fives)
            else:
                tens = after_balance // 10
                output(balance, fifties, twenties, tens)
        else:
            twenties = after_balance // 20
            output(balance, fifties, twenties)
    else:
        fifties = balance // 50
        output(balance, fifties)


if __name__ == "__main__":
    main()
