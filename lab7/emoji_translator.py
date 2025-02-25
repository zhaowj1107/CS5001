'''
File: emoji_translator.py
Author:  Weijian Zhao (David)
Date: 2025-02-19
Class: CS_5001, Spring_2025
'''

def create_emoji_dictionary():
    """
    Creates a dictionary mapping words to their corresponding emoji representations.
    Returns:
        dict: Dictionary with words as keys and emoji as values
    """
    emoji = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😡",
    "dog": "🐶",
    "cat": "🐱"
}
    return emoji

def translate_sentence(sentence: str, emoji_dict: dict[str, str]) -> str:
    """
    Translates a sentence by replacing words with their corresponding emoji.
    Args:
        sentence (str): The input sentence to translate
        emoji_dict (dict): Dictionary mapping words to emoji
    Returns:
        str: Translated sentence with words replaced by emoji
    >>> emoji_dict = {"happy": "😊", "sad": "😢"}
    >>> translate_sentence("I am happy", emoji_dict)
    'I am 😊'
    >>> translate_sentence("She is sad and happy", emoji_dict)
    'She is 😢 and 😊'
    >>> translate_sentence("No emoji here", emoji_dict)
    'No emoji here'
    """
    sentence_list = sentence.split()
    for word_index in range(len(sentence_list)):
        if sentence_list[word_index].lower() in emoji_dict:
            sentence_list[word_index] = emoji_dict[sentence_list[word_index]]
    return " ".join(sentence_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    emoji_dict = create_emoji_dictionary()
    sentence = input("Enter a sentence: ")
    translated_sentence = translate_sentence(sentence, emoji_dict)
    print(translated_sentence)