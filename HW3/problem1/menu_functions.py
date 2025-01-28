"""
File: menu_functions
Author: Weijian Zhao (David)
Date: 2025-01-27
Class: CS_5001, Spring_2025
Description: 
homework 2-1: System Functions and DateTime Menu

"""

import os
import datetime


def display_choices():
    """
    Function menu_list()
    Parameters: nothing
    Returns: print a list of menu options
    """
    print("Please choose an option:")
    print("P: Print the menu again")
    print("M: Print the current month name")
    print("W: Print the current weekday")
    print("T: print the current time")
    print("D: Print the current directory")
    print("Q: Quit\n")


def get_current_month_name():
    """
    Function get_current_month_name
    Parameters: nothing
    Returns: returns the current month name.
    """
    month_name = datetime.date.today().strftime("%B")
    return month_name


def get_current_weekday():
    """
    Function get_current_weekday
    Parameters: nothing
    Returns: returns the current weekday name.
    """
    weekday_name = datetime.date.today().strftime("%A")
    return weekday_name


def get_current_time():
    """
    Function get_current_time
    Parameters: nothing
    Returns: returns the current time.
    """
    time_name = datetime.datetime.now().strftime("%H:%M:%S")
    return time_name


def get_current_directory():
    """
    Function get_current_directory
    Parameters: nothing
    Returns: returns the current directory.
    """
    current_directory = os.getcwd()
    return current_directory


def run_menu():
    """
    Function run_menu
    Parameters: nothing
    Returns: returns the current directory.
    """
    loop_control = True
    while loop_control:
        display_choices()
        user_choice = str(input("Choice: "))
        if user_choice == "P" or user_choice == "p":
            loop_control = True
        elif user_choice == "M" or user_choice == "m":
            output_value = get_current_month_name()
            print(output_value,"\n")
            loop_control = True
        elif user_choice == "W" or user_choice == "w":
            output_value = get_current_weekday()
            print(output_value,"\n")
            loop_control = True
        elif user_choice == "T" or user_choice == "t":
            output_value = get_current_time()
            print(output_value,"\n")
            loop_control = True
        elif user_choice == "D" or user_choice == "d":
            output_value = get_current_directory()
            print(output_value,"\n")
            loop_control = True
        elif user_choice == "Q" or user_choice == "q":
            print("Goodbye!\n")
            loop_control = False
        else:
            print("Invalid choice. Please try again.\n")
            loop_control = True


if __name__ == "__main__":
    pass
