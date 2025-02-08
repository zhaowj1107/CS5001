'''
File: words_in_sentence.py
Author:  Weijian Zhao (David)
Date: 2025-02-05
Class: CS_5001, Spring_2025
'''


def take_input():
    """
    Function take_input
    Parameters: None
    Returns: str
    Prompts the user to enter a sentence and returns the input
    """
    user_str = input("Enter a sentence: ")
    return user_str


def separate_words(sentence: str):
    """
    Function separate_words
    Parameters: 
        sentence (str): The input sentence to process
    Returns: list[str]
    Processes a sentence by:
    1. Removing punctuation
    2. Splitting into individual words
    3. Returning list of words
    >>> separate_words("Hello, world!")
    ['hello', 'world']
    >>> separate_words("This is a test sentence.")
    ['this', 'is', 'a', 'test', 'sentence']
    >>> separate_words("Multiple   spaces? No problem!")
    ['multiple', 'spaces', 'no', 'problem']
    """
    PUNCTUATION = ["!", "?", ",", ".", ";", ":"]
    for symble in PUNCTUATION:
        sentence = sentence.replace(symble, "")
    sentence = sentence.lower()
    list_raw = sentence.split()
    return list_raw


def counter(list_raw: list):
    """
    Function counter
    Parameters:
        list_raw (list): A list of words to process
    Returns: tuple(list[str], list[int])
    Processes a list of words by:
    1. Creating a list of unique words
    2. Counting frequency of each unique word
    3. Returning tuple containing (unique_words, frequency)
    >>> counter(['hello', 'world', 'hello'])
    (['hello', 'world'], [2, 1])
    >>> counter(['this', 'is', 'a', 'test'])
    (['this', 'is', 'a', 'test'], [1, 1, 1, 1])
    >>> counter(['repeat', 'repeat', 'repeat'])
    (['repeat'], [3])
    """
    unique_words = []
    frequency = []
    for word in list_raw:
        if word in unique_words:
            pass
        else:
            unique_words.append(word)
    for word_exist in unique_words:
        counter = 0
        for word_raw in list_raw:
            if word_raw == word_exist:
                counter += 1
            else:
                pass
        frequency.append(counter)
    return unique_words, frequency


def output_result(word_list, unique_words, frequency):
    """
    Function output_result
    Parameters:
        word_list (list): List of all words in the sentence
        unique_words (list): List of unique words
        frequency (list): List of word frequencies corresponding
    Returns: None
    Prints formatted output showing:
    1. Total word count
    2. Each word with its index
    3. Frequency of each unique word
    """
    print(f"You typed {len(word_list)} words in that sentence.")
    print("Here are the individual words:")
    for index_raw in range(len(word_list)):
        print(f"{index_raw}. {word_list[index_raw]}")
    print("The frequency of each word is:")
    for index_unique in range(len(unique_words)):
        print(f"{unique_words[index_unique]} : {frequency[index_unique]}")
