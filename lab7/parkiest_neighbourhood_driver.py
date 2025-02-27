'''
File: parkiest_neighbourhood_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-19
Class: CS_5001, Spring_2025
'''


import parkiest_neighbourhood_functions as pnf


def main():
    """
    Function: main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    try:
        # Safely read file and handle potential errors
        list1, list2 = pnf.read_from_file("parks_name_neighbourhood.txt")
        if not list1 or not list2:
            print("Error: No data was read from the file")
            return
        # Safely construct dictionary and handle potential errors
        dict_park = pnf.construct_park_dictionary(list1, list2)
        if not dict_park:
            print("Error: Could not construct park dictionary")
            return
        # Safely display parks and handle potential errors
        try:
            pnf.display_parks_and_neighbourhood(dict_park)
        except Exception as e:
            print(f"Error displaying parks: {e}")
        # Safely display park counts and handle potential errors
        try:
            dict_park_counter = pnf.count_neighbourhood_parks(dict_park)
            pnf.display_parks_per_neighbourhood(dict_park)
        except Exception as e:
            print(f"Error displaying park counts: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
