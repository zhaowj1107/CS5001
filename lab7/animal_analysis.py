'''
File: animal_analysis.py
Author:  Weijian Zhao (David)
Date: 2025-02-19
Class: CS_5001, Spring_2025
'''


def create_name_dictionary(com_name, sci_name):
    """
    Creates a dictionary mapping common bird names to scientific names.
    Args:
        com_name (list): List of common bird names
        sci_name (list): List of scientific names corresponding to common names
    Returns:
        dict: Dictionary with common names as keys and scientific names
    >>> create_name_dictionary(['Robin'], ['Turdus migratorius'])
    {'Robin': 'Turdus migratorius'}
    """
    dict_animal = {}
    for com_name_idx in range(len(com_name)):
        dict_animal[com_name[com_name_idx]] = sci_name[com_name_idx]
    return dict_animal


def create_names_habitat_dictionary(com_name, sci_name, nest_type):
    """
    Creates a dictionary mapping common bird names to both scientific
    Args:
        com_name (list): List of common bird names
        sci_name (list): List of scientific names corresponding to common name
        nest_type (list): List of nest types corresponding to common names
    >>> create_names_habitat_dictionary(['Robin'], ['Tur'], ['Cup'])
    {'Robin': ['Tur', 'Cup']}
    >>> create_names_habitat_dictionary(['Spa'], ['Pas'], ['Cav'])
    {'Spa': ['Pas', 'Cav']}
    """
    dict_animal = {}
    for com_name_idx in range(len(com_name)):
        dict_animal[com_name[com_name_idx]] = [sci_name[com_name_idx], 
                                               nest_type[com_name_idx]]
    return dict_animal


def count_habitat_type(habit_dict, nest_habit_str):
    """
    Counts the number of birds that have a specific nest habitat type.
    Args:
        habit_dict (dict): Dictionary mapping bird names
        nest_habit_str (str): The nest habitat type to count
    Returns:
        int: Number of birds with the specified nest habitat type
    >>> count_habitat_type({'Robin': 'Cup', 'Sparrow': 'Cavity'}, 'Cup')
    1
    >>> count_habitat_type({'Eag': 'Platform', 'Owl': 'Platform'}, 'Platform')
    2
    >>> count_habitat_type({'Penguin': 'Burrow', 'Duck': 'Ground'}, 'Tree')
    0
    """
    counter = 0
    for bird_habit in habit_dict.values():
        if nest_habit_str == bird_habit:
            counter += 1
    return counter


if __name__ == "__main__":
    pass
