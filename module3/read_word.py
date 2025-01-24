'''
File: read_word.py
Author: Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025
Description: 
code practice 3-4: read_word

'''

def read_word():
    '''
    Function read_word()
    Parameters: None
    Returns: None
    '''
    memory_word = ""
    input_word = ""
    while input_word != "stop":
        input_word = input("Enter a word: ")
        if input_word == "stop":
            continue
        else:
            memory_word = memory_word + input_word + " "
    print(memory_word)
if __name__ == "__main__":
    read_word()