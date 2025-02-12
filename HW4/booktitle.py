"""
File: booktitle
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
homework 4-1: Recipe Ingredient Scrubber
"""


def is_length_valid(title: str, min_length: int = 12, max_length: int = 25):
    """
    function name: is_length_valid
    checks if the title length is within valid range (inclusive)
    >>> is_length_valid("Short")
    False
    >>> is_length_valid("Short", 1)
    True
    >>> is_length_valid("Short", 1, 3)
    False
    >>> is_length_valid("This is a valid title")
    True
    >>> is_length_valid("too long to be valid with default parameters")
    False
    >>> is_length_valid("long but be valid with parameters", 1, 40)
    True
    >>> is_length_valid("Exactly 12 chars")
    True
    >>> is_length_valid("Exact 25 characters long!")
    True
    """
    if min_length <= len(title) <= max_length:
        return True
    else:
        return False


def has_capital_letters(title: str, num: int = 1):
    """
    function name: has_capital_letters
    checks if the title contains at least one capital letter

    >>> has_capital_letters("Valid Title", 1)
    True
    >>> has_capital_letters("valid title")  # No capitals
    False
    >>> has_capital_letters("Title With Multiple Capitals", 4)  # Multiple capitals
    True
    >>> has_capital_letters("title with Capital in middle", 1)
    True
    >>> has_capital_letters("title with Capital in middle", 2)
    False
    >>> has_capital_letters("TITLE ending with A", 5)  # Capital at end
    True
    >>> has_capital_letters("123 Title", 2)  # Capital after numbers
    False
    >>> has_capital_letters("!@#Title")  # Capital after symbols
    True
    """
    UPPER_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    for letter in UPPER_ALPHA:
        counter += title.count(letter)
    if counter >= num:
        return True
    else:
        return False


def has_lowercase_letters(title: str, num: int = 2):
    """
    function name: has_lowercase_letters
    checks if the title contains at least one lowercase letters

    >>> has_lowercase_letters("Title with lowercase", 1)
    True
    >>> has_lowercase_letters("TITLE WITHOUT LOWERCASE")
    False
    >>> has_lowercase_letters("Title With Mixed Case", 20)
    False
    >>> has_lowercase_letters("TITLE WITH ONE LOWERCASe")
    False
    >>> has_lowercase_letters("TITLE WITH 1 LOWERCASE a", 0)
    True
    """
    LOWER_ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0
    for letter in LOWER_ALPHA:
        counter += title.count(letter)
    if counter >= num:
        return True
    else:
        return False


def has_numbers(title: str, num: int = 1):
    """
    function name: has_numbers
    checks if the title contains at least one number

    >>> has_numbers("Title with 1 number")
    True
    >>> has_numbers("Title without numbers")
    False
    >>> has_numbers("Title without numbers", 0)
    True
    >>> has_numbers("Title with 123 numbers", 3)
    True
    >>> has_numbers("Title with number at end1", 2)
    False
    >>> has_numbers("1Title starting with number")
    True
    """
    NUMBER = '1234567890'
    counter = 0
    for num_1 in NUMBER:
        counter += title.count(num_1)
    if counter >= num:
        return True
    else:
        return False


def has_special_characters(title: str, num: int = 1):
    """
    function name: has_special_characters
    checks if the title contains at least one special character from !.;:&

    >>> has_special_characters("Title with! special")
    True
    >>> has_special_characters("Title without special", 0)
    True
    >>> has_special_characters("Title without special")
    False
    >>> has_special_characters("Title with:::: special", 3)
    True
    >>> has_special_characters("Title with. special")
    True
    >>> has_special_characters("Title with& special", 2)
    False
    """
    SPECIAL = '!.;:&'
    counter = 0
    for symbol in SPECIAL:
        counter += title.count(symbol)
    if counter >= num:
        return True
    else:
        return False


def validate_booktitle(title: str):
    """
    function name: validate_booktitle
    validates if a book title meets all requirements:
    - Length between 12 and 25 characters
    - Contains at least 1 capital letter
    - Contains at least 2 lowercase letters
    - Contains at least 1 number
    - Contains at least 1 special character (!.;:&)
    >>> validate_booktitle("Valid Title 123!")
    True
    >>> validate_booktitle("TooShort 1!")
    False
    >>> validate_booktitle("This Title Is Way Too Long To Be Valid 123!")
    False
    >>> validate_booktitle("no capitals here 123!")
    False
    >>> validate_booktitle("ALL CAPS NO LOWERCASE 123!")
    False
    >>> validate_booktitle("Missing Numbers Here!")
    False
    >>> validate_booktitle("Missing Special Chars 123")
    False
    """
    if not (is_length_valid(title)):
        return False
    if not (has_capital_letters(title)):
        return False
    if not (has_lowercase_letters(title)):
        return False
    if not (has_numbers(title)):
        return False
    if not (has_special_characters(title)):
        return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
