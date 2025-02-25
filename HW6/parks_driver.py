"""
File: parks_driver.py
Author: Weijian Zhao(David)
Date: 2025-02-24
Class: CS_5001, Spring_2025
Description: 
homework 6: Parks and Neighbourhoods
"""

import parks_functions as pf


def main():
    """
    Function: main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    list_1 = pf.read_from_file("parks.txt")
    # print(list_1)
    dict_1 = pf.construct_park_dictionary(list_1)
    # print(dict_1)
    most_parks_neigh = pf.get_neighbourhood_with_most_parks(dict_1)
    # print(most_parks_neigh)
    print(f"The neighbourhood with the most parks is {most_parks_neigh}.\n")
    print(f"Parks in {most_parks_neigh}:")
    for park in pf.get_parks_in_neighbourhood(dict_1, most_parks_neigh):
        print(f"- {park}")


if __name__ == "__main__":
    main()
