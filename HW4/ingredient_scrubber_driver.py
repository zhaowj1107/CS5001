"""
File: ingredient_scrubber_driver
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
homework 4-1: Recipe Ingredient Scrubber
"""

import ingredient_scrubber as ins


def main():
    """
    Function main
    Parameters: None
    Returns: Nothing
    Get user input and print out the result
    """
    user_input_list = []
    cleaned_output_list = []
    flag_list = []
    FLAG = "Invalid"
    loop_control = True

    while loop_control:
        user_input = str(input("Enter ingredient entry: "))
        if user_input.lower() == 'done':
            loop_control = False
        else:
            user_input_list.append(user_input)

    for user_input in user_input_list:
        output = ins.scrub_ingredient(user_input)
        cleaned_output_list.append(output)
        if output.find(FLAG) != -1:
            flag_list.append(output)
    print("")
    print("Scrubbed Ingredients: ")
    for output in cleaned_output_list:
        print(output)

    # Print flagged if necessary
    if flag_list != []:
        print("")
        print("Flagged Entries: ")
        for flag_output in flag_list:
            print(f"- {flag_output}")
    else:
        pass


if __name__ == "__main__":
    main()
