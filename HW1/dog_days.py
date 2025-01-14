'''
File: dog_days.py
Author: Weijian Zhao (David)
Date: 2025-01-13
Class: CS_5001, Spring_2025
Description: 
homework 1-2: Dog Adoption Packages

Test case #1:
Input: 1 year old, 0 bags of dog food, 0 dog toys, no permit
Output: $150

Test case #2:
Input: 1 year old, 3 bags of dog food, 3 dog toys, with a permit
Output: 241

Test case #3:
Input: 4 year old, 2 bags of dog food, 0 dog toys, no permit
Output: $142.5

Test case #4:
Input: 4 year old, 3 bags of dog food, 2 dog toys, with a permit
Output: 203.25

'''


def main():

    BASE_FEE = 150
    DISCOUNT = 0.25
    BAGS_PRICE = 20
    DOG_TOYS_PRICE = 10
    DOG_PERMIT_PRICE = 41

    print("Welcome to the Happy Dog Day Shelter!")
    print("Thank you for adopting a dog today.")
    print("We have a few questions for you.")
    dog_age = int(input("How old is the dog you're adopting? "))
    num_bags = int(input("How many bags of dog food would you like? "))
    num_toys = int(input("How many dog toys would you like? "))
    dog_permit = input("Do you need a dog permit? (Y/N) ")
    if dog_permit == "Y":
        dog_permit = 1
    else:
        dog_permit = 0

    total_cost = (
        BASE_FEE + 
        (BAGS_PRICE * num_bags) + 
        (DOG_TOYS_PRICE * num_toys) + 
        (dog_permit * DOG_PERMIT_PRICE)
    )
    if total_cost > 200:
        if dog_age > 3:
            total_cost_final = min(
                total_cost - 40, total_cost * (1 - DISCOUNT)
            )
        else:
            total_cost_final = total_cost - 40
    else:
        if dog_age > 3:
            total_cost_final = total_cost * (1 - DISCOUNT)
        else:
            total_cost_final = total_cost

    print(f"The total cost of your adoption is {total_cost_final}")


if __name__ == "__main__":
    main()
