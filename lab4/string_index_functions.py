def return_letter_index(str: str, letter: str):
    """
    Function return_letter_index
    Parameters: 
        str (str): The string to search through
        letter (str): The single character to find in the string
    Returns: int or str: The index 
    Finds and returns the index of the first occurrence of a letter
    If the letter is not found, returns an empty string.
    >>> return_letter_index("hello", "e")
    1
    >>> return_letter_index("world", "d")
    4
    >>> return_letter_index("python", "z")
    ''
    >>> return_letter_index("mississippi", "s")
    2
    """
    for index in range(len(str)):
        if str[index] == letter:
            return index
    return ""


def return_index_letter(str: str, index: int):
    """
    Function return_index_letter
    Parameters:
        str (str): The string to search through
        index (int): The index position to retrieve
    Returns: str or int: The character at the given index or -1
    Retrieves and returns the character at a specific index in a string.
    If the index is out of bounds, returns -1.
    >>> return_index_letter("hello", 1)
    'e'
    >>> return_index_letter("world", 4)
    'd'
    >>> return_index_letter("python", 10)
    -1
    >>> return_index_letter("mississippi", 2)
    's'
    """
    if 0 < index <= len(str) - 1:
        return str[index]
    else:
        return -1
    return ""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
