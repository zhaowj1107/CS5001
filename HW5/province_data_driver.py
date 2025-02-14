"""
File: province_data_driver.py
Author: Weijian Zhao (David)
Date: 2025-02-13
Class: CS_5001, Spring_2025
Description: 
homework 5-2: Provinces Data Dictionary
"""


import province_data_analysis as pda
from territory_province_data import PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS

def main():
    """
    Function: main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    province_in_lists = pda.create_data_dictionary_by_province_in_lists(PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE)
    dict_by_province = pda.create_dictionary_by_province("Alberta", PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS)
    dict_of_dict = pda.create_dictionary_of_dictionaries_by_province(PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS)
    dict_by_BC = pda.create_dictionary_by_province("British Columbia", PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS)
    dict_by_yukon = pda.create_dictionary_by_province("Yukon", PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS)
    dict_by_nu = pda.create_dictionary_by_province("Nunavut", PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS)
    dict_by_Quebec = pda.create_dictionary_by_province("Quebec", PROVINCE_NAMES, POPULATION, AREA, IS_PROVINCE, HEADERS)
    quebec_density = round(dict_by_Quebec['Population'] / dict_by_Quebec['Area'], 2)

    # output
    print("Number of keys in each dictionary:")
    print(f"create_data_dictionary_by_province_in_lists: {len(province_in_lists)}")
    print(f"create_dictionary_by_province: {len(dict_by_province)}")
    print(f"dictionary_of_dictionaries_by_province: {len(dict_of_dict)}")
    print(f"British Columbia's population: {dict_by_BC['Population']:,}")
    # numbers with thousands separators is needed
    print(f"Yukon's area: {dict_by_yukon['Area']:,.2f}")
    print(f"Is Nunavut a province? {dict_by_nu['Is Province?']}")
    print(f"Population density of Quebec: {quebec_density:,.2f} people per square km")


if __name__ == "__main__":
    main()
