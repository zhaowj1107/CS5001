'''
File: find_pm.py
Author: Weijian Zhao (David)
Date: 2025-01-20
Class: CS_5001, Spring_2025
Description: 
homework 2-1: Who was the Prime Minister?
'''


def get_input_year():
    '''
    Function get_input_year()
    Parameters: none
    Returns: year
    '''
    year = int(input('For which year you like to look up the PM of Canada? '))
    return year


def find_prime_minister(year):
    '''
    Function find_prime_minister()
    Parameters: year
    Returns: the full name of Canadian prime minister. 
    >>> find_prime_minister(1993)
    'Jean Chrétien'
    >>> find_prime_minister(2003)
    'Paul Martin'
    >>> find_prime_minister(2006)
    'Stephen Harper'
    >>> find_prime_minister(2015)
    'Justin Trudeau'
    >>> find_prime_minister(2025)
    No prime minister found for this year.
    Please enter a year between 1993 and 2024.
    >>> find_prime_minister(1985)
    No prime minister found for this year.
    Please enter a year between 1993 and 2024.

    '''
    if year >= 1993 and year < 2003:
        name = 'Jean Chrétien'
    elif year >= 2003 and year < 2006:
        name = 'Paul Martin'
    elif year >= 2006 and year < 2015:
        name = 'Stephen Harper'
    elif year >= 2015 and year < 2025:
        name = 'Justin Trudeau'
    else:
        print('No prime minister found for this year.')
        print('Please enter a year between 1993 and 2024.')
        return None
    return name


def find_party(name):
    '''
    Function find_party()
    Parameters: name
    Returns: the party of Canadian prime minister. 
    >>> find_party('Jean Chrétien')
    'Liberal'
    >>> find_party('Paul Martin')
    'Liberal'
    >>> find_party('Stephen Harper')
    'Conservative'
    >>> find_party('Justin Trudeau')
    'Liberal'
    >>> find_party('Donald Trump')
    Invalid name or input.
    Please enter the correct PM name.
    '''
    if name is None:
        return None
    if name == 'Jean Chrétien':
        party = 'Liberal'
    elif name == 'Paul Martin':
        party = 'Liberal'
    elif name == 'Stephen Harper':
        party = 'Conservative'
    elif name == 'Justin Trudeau':
        party = 'Liberal'
    else:
        print('Invalid name or input.')
        print('Please enter the correct PM name.')
        return None
    return party


def output_pm(year, name, party):
    '''
    Function output_pm()
    Parameters: name, party
    Returns: None
    >>> output_pm(1993, 'Jean Chrétien', 'Liberal')
    In 1993 the Prime Minister was Jean Chrétien, Liberal
    >>> output_pm(2003, 'Paul Martin', 'Liberal')
    In 2003 the Prime Minister was Paul Martin, Liberal
    >>> output_pm(2006, 'Stephen Harper', 'Conservative')
    In 2006 the Prime Minister was Stephen Harper, Conservative
    >>> output_pm(2015, 'Justin Trudeau',  'Liberal')
    In 2015 the Prime Minister was Justin Trudeau, Liberal

    '''
    if name is None or party is None:
        return None
    print(f'In {year} the Prime Minister was {name}, {party}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
