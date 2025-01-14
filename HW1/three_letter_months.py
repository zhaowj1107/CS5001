'''
File: three_letter_months.py.py
Author: Weijian Zhao (David)
Date: 2025-01-13
Class: CS_5001, Spring_2025
Description: 
homework 1-3: Three-letter months
'''


def main():
    month_input = input("Enter a month: ")

    if month_input == "Jan" or month_input == "1" or month_input == "January":
        print("January has 31 days.")
    elif (
        month_input == "Feb" or month_input == "2" or 
        month_input == "February"
    ):
        print("February has 28 days.")
    elif month_input == "Mar" or month_input == "3" or month_input == "March":
        print("March has 31 days.")
    elif month_input == "Apr" or month_input == "4" or month_input == "April":
        print("April has 30 days.")
    elif month_input == "May" or month_input == "5" or month_input == "May":
        print("May has 31 days.")
    elif month_input == "Jun" or month_input == "6" or month_input == "June":
        print("June has 30 days.")
    elif month_input == "Jul" or month_input == "7" or month_input == "July":
        print("July has 31 days.")
    elif month_input == "Aug" or month_input == "8" or month_input == "August":
        print("August has 31 days.")
    elif (
        month_input == "Sep" or month_input == "9" or 
        month_input == "September"
    ):
        print("September has 30 days.")
    elif (
        month_input == "Oct" or month_input == "10" or 
        month_input == "October"
    ):
        print("October has 31 days.")
    elif (
        month_input == "Nov" or month_input == "11" or 
        month_input == "November"
    ):
        print("November has 30 days.")
    elif (
        month_input == "Dec" or month_input == "12" or 
        month_input == "December"
    ):
        print("December has 31 days.")
    else:
        print("Please enter a valid month.")


if __name__ == "__main__":
    main()
