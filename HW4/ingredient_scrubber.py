"""
File: ingredient_scrubber
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
homework 4-1: Recipe Ingredient Scrubber
"""


def parse_entry(entry: str):
    """
    function name: parse_entry
    splits str into three components: quantity, unit, and ingredient name.
    >>> parse_entry("1 cup of flour")
    ['1', 'cup', 'of flour']
    >>> parse_entry("2 tablespoons of sugar")
    ['2', 'tablespoons', 'of sugar']
    >>> parse_entry("1/2 cups of milk")
    ['1/2', 'cups', 'of milk']
    >>> parse_entry("12 ounces of chocolate chips")
    ['12', 'ounces', 'of chocolate chips']
    >>> parse_entry("1 pinch of cinnamon")
    ['1', 'pinch', 'of cinnamon']
    """
    list_result = []
    seperate_index = entry.rfind("of")
    for str in entry[:seperate_index].split():
        list_result.append(str)
    ingredient = entry[seperate_index:]
    list_result.append(ingredient)
    return list_result


def validate_unit(unit: str):
    """
    function name: validate_unit
    Checks if the unit is valid and converts plural units to singular
    >>> validate_unit("cups")
    'cup'
    """
    unit_list = [
        "teaspoon", "cup", 
        "tablespoon", "gram", "liter"
    ]
    if unit[-1] == "s":
        unit_singular = unit[:-1]
    else:
        unit_singular = unit
    if unit_singular in unit_list:
        return unit_singular
    else:
        return "Invalid Unit"


def validate_quantity(quantity: str):
    """
    function name: validate_quantity
    checks if the quantity is a valid number (integer or float)
    >>> validate_quantity("1")
    True
    >>> validate_quantity("1.2")
    True
    >>> validate_quantity("three")
    False
    >>> validate_quantity("")
    False
    """
    quantity = quantity.replace(".", "")
    if quantity.isdigit():
        return True
    else:
        return False


def validate_ingredient(ingredient: str):
    """
    function name: validate_unit
    Checks if the unit is valid and converts plural units to singular
    >>> validate_ingredient("of flour")
    'flour'
    >>> validate_ingredient("peppersss")
    'Invalid Ingredient'
    >>> validate_ingredient("and baking soda")
    'baking soda'
    >>> validate_ingredient("in baking soda")
    'baking soda'
    >>> validate_ingredient("with baking soda")
    'baking soda'
    >>> validate_ingredient("of wa1ter")
    'Invalid Ingredient'
    >>> validate_ingredient("of_water")
    'Invalid Ingredient'
    """
    conn_words = ["of ", "and ", "with ", "in "]
    for word in conn_words:
        if ingredient.find(word) != -1:
            ingredient = ingredient.replace(word, "")
    ingredient_clean = ingredient.rstrip()
    if not (ingredient_clean.replace(" ", "").isalpha()):
        return "Invalid Ingredient"
    else:
        for letter in range(len(ingredient_clean) - 2):
            if ingredient_clean[letter] == ingredient_clean[letter + 1] == ingredient_clean[letter + 2]:
                return "Invalid Ingredient"
        return ingredient_clean
    pass


def scrub_ingredient(entry: str):
    """
    >>> scrub_ingredient("1 cups of floor")
    '1 cup floor'
    >>> scrub_ingredient("2 tablespoons of sugar ")
    '2 tablespoon sugar'
    >>> scrub_ingredient("three teaspoon salt")
    'Invalid Quantity: three teaspoon salt'
    >>> scrub_ingredient("1.5 liters of water")
    '1.5 liter water'
    >>> scrub_ingredient("half teaspoon of baking soda")
    'Invalid Quantity: half teaspoon of baking soda'
    >>> scrub_ingredient("1.25 liters of milk")
    '1.25 liter milk'
    >>> scrub_ingredient("1 cups of peppersss")
    'Invalid Ingredient: 1 cups of peppersss'
    >>> scrub_ingredient("4 tablespoons of cocoa powder")
    '4 tablespoon cocoa powder'
    >>> scrub_ingredient("0.5 liltes of olive oil")
    'Invalid Unit: 0.5 liltes of olive oil'
    >>> scrub_ingredient("1 cup of flour")
    '1 cup flour'
    >>> scrub_ingredient("2 tablespoons of sugar")
    '2 tablespoon sugar'
    >>> scrub_ingredient("1 gram of sugar")
    '1 gram sugar'
    >>> scrub_ingredient("1.5 liters of milk")
    '1.5 liter milk'
    """
    list_result = []
    list_result = parse_entry(entry)
    if validate_quantity(list_result[0]):
        quantity = list_result[0]
    else:
        return (f"Invalid Quantity: {entry}")

    if validate_unit(list_result[1]) == "Invalid Unit":
        return (f"Invalid Unit: {entry}")
    else:
        unit = validate_unit(list_result[1])

    if validate_ingredient(list_result[2]) == "Invalid Ingredient":
        return (f"Invalid Ingredient: {entry}")
    else:
        ingredient = validate_ingredient(list_result[2])

    return quantity + " " + unit + " " + ingredient


if __name__ == "__main__":
    import doctest
    doctest.testmod()
