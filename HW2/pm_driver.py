'''
File: pm_deriver.py
Author: Weijian Zhao (David)
Date: 2025-01-20
Class: CS_5001, Spring_2025
Description: 
homework 2-1: Who was the Prime Minister?

'''
import find_pm as pm


def main():
    """
    Function main()
    Parameters: none
    Returns: None
    """
    year = pm.get_input_year()
    name = pm.find_prime_minister(year)
    party = pm.find_party(name)
    pm.output_pm(year, name, party)


if __name__ == "__main__":
    main()
