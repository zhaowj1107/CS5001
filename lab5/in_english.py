'''
File: words_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-12
Class: CS_5001, Spring_2025
'''


def translate(integer: int):
    '''
    Translates a single digit integer to its English word equivalent.
    Args:
        integer (int): The digit to translate (0-9)
    Returns:
        str: English word for the digit
    >>> translate(0)  # Test zero case
    'zero'
    >>> translate(5)  # Test middle case
    'five'
    >>> translate(9)  # Test upper bound
    'nine'
    >>> translate(10)  # Test out of range
    'number out of range'
    '''
    if integer == 0:
        return "zero"
    elif integer == 1:
        return "one"
    elif integer == 2:
        return "two"
    elif integer == 3:
        return "three"
    elif integer == 4:
        return "four"
    elif integer == 5:
        return "five"
    elif integer == 6:
        return "six"
    elif integer == 7:
        return "seven"
    elif integer == 8:
        return "eight"
    elif integer == 9:
        return "nine"
    else:
        return "number out of range"


def in_english(number):
    '''
    Converts a number to its English word representation.
    Args:
        number (int): The number to convert (0-999)
    Returns:
        str: English words representing the number
    >>> in_english(0)  # Test zero case
    'zero'
    >>> in_english(5)  # Test single digit
    'five'
    >>> in_english(123)  # Test multiple digits
    'one two three'
    >>> in_english(999)  # Test upper bound
    'nine nine nine'
    >>> in_english(1000)  #
    'one zero zero zero'
    '''
    # result_str = ""
    # if number == 0:
    #     return ""
    # else:
    #     last_digit = number % 10
    #     result_str = translate(last_digit)
    #     return (in_english(number // 10) + " " + result_str).strip()
    number = str(number)
    result_str = ""
    if number == "":
        return ""
    else:
        last_digit = int(number[0])
        return (translate(last_digit) + " " + in_english(number[1:])).strip()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
