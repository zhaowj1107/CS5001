'''
File: wbird_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-19
Class: CS_5001, Spring_2025
'''

import animal_analysis as aa
from bird_constants import COMMON_BIRDS, SCIENTIFIC_BIRDS, NEST_TYPES


def main():
    """
    Function: main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    print("Question #1: The dict return like below:")
    print(aa.create_name_dictionary(COMMON_BIRDS, SCIENTIFIC_BIRDS))
    print("")
    print("Question #2: The dict return like below:")
    print(aa.create_names_habitat_dictionary(COMMON_BIRDS, 
                                             SCIENTIFIC_BIRDS, NEST_TYPES))
    print("")
    habitats_str = 'platform'
    dict_habit = aa.create_name_dictionary(COMMON_BIRDS, NEST_TYPES)
    result = aa.count_habitat_type(dict_habit, habitats_str)
    print(f"Question #3: The number of {habitats_str} is {result}")


if __name__ == "__main__":
    main()
