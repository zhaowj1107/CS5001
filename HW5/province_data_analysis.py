"""
File: province_data_analysis.py
Author: Weijian Zhao (David)
Date: 2025-02-13
Class: CS_5001, Spring_2025
Description: 
homework 5-2: Provinces Data Dictionary
for this problem, stylecheck will ignore the length limitation
"""


def create_data_dictionary_by_province_in_lists(province_names: list, population: list, area: list, is_province: list):
    """
    This function creates a dictionary where each key is a province name and 
    each value is a list containing the corresponding population, area, 
    and province status (True/False).
    Parameters:
        province_names: list of province/territory names
        population: list of population numbers
        area: list of area sizes in square kilometers
        is_province: list of booleans indicating province status
    Returns:
        dictionary mapping province names to their data as lists
    >>> create_data_dictionary_by_province_in_lists(["BC", "AB"], [1, 2], [10.0, 20.0], [True, False])
    {'BC': [1, 10.0, True], 'AB': [2, 20.0, False]}
    """
    province_list = {}
    length = len(province_names)
    for name_index in range(length):
        province_list[province_names[name_index]] = [population[name_index], area[name_index], is_province[name_index]]
    return province_list


def create_dictionary_by_provinces(province_names: list, population: list, area: list, is_province: list, headers: list):
    """
    This function creates a dictionary where each key is a header name and 
    each value is a list containing all values for that category across provinces.
    Parameters:
        province_names: list of province/territory names
        population: list of population numbers
        area: list of area sizes in square kilometers
        is_province: list of booleans indicating province status
        headers: list of header names for the data categories
    Returns:
        dictionary mapping headers to lists of all values for that category
    >>> create_dictionary_by_provinces(["BC", "AB"], [1, 2], [10.0, 20.0], [True, False], ["Name", "Pop", "Area", "Prov?"])
    {'Name': ['BC', 'AB'], 'Pop': [1, 2], 'Area': [10.0, 20.0], 'Prov?': [True, False]}
    """
    list_value = [province_names, population, area, is_province]
    province_list = dict(zip(headers, list_value))
    return province_list


def create_dictionary_by_province(province_name, province_names: list, population: list, area: list, is_province: list, headers: list):
    """
    This function creates a dictionary for a specific province where each key is a header name and 
    each value is the corresponding data for that province.
    Parameters:
        province_name: name of the province to create dictionary for
        province_names: list of province/territory names
        population: list of population numbers
        area: list of area sizes in square kilometers
        is_province: list of booleans indicating province status
        headers: list of header names for the data categories
    Returns:
        dictionary mapping headers to values for the specific province
    >>> create_dictionary_by_province("BC", ["BC", "AB"], [1, 2], [10.0, 20.0], [True, False], ["Name", "Pop", "Area", "Prov?"])
    {'Name': 'BC', 'Pop': 1, 'Area': 10.0, 'Prov?': True}
    """
    name_index = province_names.index(province_name)
    list_value = [province_names[name_index], population[name_index], area[name_index], is_province[name_index]]
    province_list = dict(zip(headers, list_value))
    return province_list


def create_dictionary_of_dictionaries_by_province(province_names: list, population: list, area: list, is_province: list, headers: list):
    """
    This function creates a dictionary where each key is a province name and 
    each value is a dictionary containing all data for that province.
    Parameters:
        province_names: list of province/territory names
        population: list of population numbers
        area: list of area sizes in square kilometers
        is_province: list of booleans indicating province status
        headers: list of header names for the data categories
    Returns:
        dictionary mapping province names to their corresponding data dictionaries
    >>> create_dictionary_of_dictionaries_by_province(["BC", "AB"], [1, 2], [10.0, 20.0], [True, False], ["Name", "Pop", "Area", "Prov?"])
    {'BC': {'Name': 'BC', 'Pop': 1, 'Area': 10.0, 'Prov?': True}, 'AB': {'Name': 'AB', 'Pop': 2, 'Area': 20.0, 'Prov?': False}}
    """
    province_list = {}
    length = len(province_names)
    for name_index in range(length):
        value = create_dictionary_by_province(province_names[name_index], province_names, population, area, is_province, headers)
        province_list[province_names[name_index]] = value
    return province_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # from territory_province_data import PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS
    # print(create_data_dictionary_by_province_in_lists(PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE))
    # print(create_dictionary_by_province("Alberta", PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS))
    # print(create_dictionary_of_dictionaries_by_province(PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS))
