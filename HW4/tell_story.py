"""
File: tell_story.py
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
homework 4-3: Tell Me a Story
"""


def get_story_ending(ending: str):
    """
    Determines the story ending based on user input.
    Parameters:
        ending (str): The type of ending desired ('stars', 'sun', or any other value)
    Returns:
        str: A string containing the appropriate ending sentence
    Doctests:
    >>> get_story_ending('stars')
    'As the stars twinkled overhead, dreams of tomorrow awaited.'
    >>> get_story_ending('sun')
    'Rest now, for when the sun rises, a new story unfolds.'
    >>> get_story_ending('moon')
    'In the quiet of the night, dreams of new adventures took flight.'
    >>> get_story_ending('STARS')
    'As the stars twinkled overhead, dreams of tomorrow awaited.'
    """

    if ending.lower() == 'stars':
        return "As the stars twinkled overhead, dreams of tomorrow awaited."
    elif ending.lower() == 'sun':
        return "Rest now, for when the sun rises, a new story unfolds."
    else:
        return "In the quiet of the night, dreams of new adventures took flight."


def process_direction(sentences: list, direction: str):
    """
    Processes a list of sentences based on the specified direction.
    Parameters:
        sentences (list): A list of strings containing story sentences
        direction (str): The direction to process the sentences ('forward', 'backward', or 'every other')
    Returns:
        list: A new list of sentences processed according to the direction
    Doctests:
    >>> process_direction(['a', 'b', 'c'], 'forward')
    ['a', 'b', 'c']
    >>> process_direction(['a', 'b', 'c'], 'backward')
    ['c', 'b', 'a']
    >>> process_direction(['a', 'b', 'c', 'd'], 'every other')
    ['a', 'c']
    >>> process_direction(['a'], 'forward')
    ['a']
    >>> process_direction(['a', 'b'], 'backward')
    ['b', 'a']
    """
    new_sentences = []
    if direction.lower() == 'forward':
        return sentences
    elif direction.lower() == 'backward':
        for line_index in range(len(sentences) - 1, -1, -1): # range from the last index to the first index
            new_sentences.append(sentences[line_index])
        return new_sentences
    else:
        for line_index in range(0, len(sentences), 2): # range from the first index with step 2
            new_sentences.append(sentences[line_index])
        return new_sentences


def generate_story(sentences: list, direction: str, ending: str):
    """
    Function generate_story
    Parameters: one list and two strs
    Returns: new_sentences_str
    >>> story = ["First", "Second", "Third"]
    >>> generate_story(story, 'backward', 'sun')
    'Third\\nSecond\\nFirst\\nRest now, for when the sun rises, a new story unfolds.'

    >>> story = ["First", "Second", "Third"]
    >>> generate_story(story, 'forward', 'stars')
    'First\\nSecond\\nThird\\nAs the stars twinkled overhead, \
dreams of tomorrow awaited.'

    >>> story = ["First", "Second", "Third"]
    >>> generate_story(story, 'every other', 'anything')
    'First\\nThird\\nIn the quiet of the night, dreams of new adventures took flight.'
    """
    # there are huge amount of return for the doctest
    new_sentences = process_direction(sentences, direction)
    new_sentences.append(get_story_ending(ending))
    new_sentences_str = "\n".join(new_sentences)
    return new_sentences_str


if __name__ == "__main__":
    import doctest
    doctest.testmod()
