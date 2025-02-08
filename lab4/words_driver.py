'''
File: words_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-05
Class: CS_5001, Spring_2025
'''
import words_in_sentence as wis


def main():
    """
    function name: main
    input: nothing
    output: none
    call the functions and print all things
    """
    user_str = wis.take_input()
    list_raw = wis.separate_words(user_str)
    unique_words, frequency = wis.counter(list_raw)
    wis.output_result(list_raw, unique_words, frequency)


if __name__ == "__main__":
    main()
