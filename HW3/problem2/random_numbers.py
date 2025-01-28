"""
File: random_numbers
Author: Weijian Zhao (David)
Date: 2025-01-27
Class: CS_5001, Spring_2025
Description: 
homework 2-1: Guessing Game
"""

import random

def generate_target():
    """
    Function generate_target()
    Parameters: nothing
    Returns: randome integer value from 1 to 100(inclusive)
    """
    random_number = random.randint(1, 100)
    return random_number

def evaluate_guess(guess: int, target: int):
    """
    Function evaluate_guess()
    Parameters: guess (int), target (int)
    Returns: True if guess is correct, False otherwise
    >>> evaluate_guess()

    """
    if guess == target:
        return "correct"
    elif guess < target:
        return "low"
    else:
        return "high"

def get_player_guess(attempt_number: int):
    """
    Function get_player_guess()
    Parameters: attempt_number (int)
    Returns: player's guess (int)
    """
    user_input = int(input(f"Guess #{attempt_number}: "))
    return user_input

def ask_to_play_again():
    """
    Function ask_to_play_again()
    Parameters: nothing
    Returns: True if player wants to play again, False otherwise
    """
    user_input = input("Would you like to play again? (y/n): ")
    return user_input == "y" or user_input == "Y"

def play_round():
    """
    Function ask_to_play_again()
    Parameters: nothing
    Returns: play one round of game
    """
    attempt_number = 1
    #generate the target number
    loop_control_round = True
    target_number = generate_target()
    while attempt_number <= 5 and loop_control_round:
        guess_number = int(get_player_guess(attempt_number))
        result = evaluate_guess(guess_number, target_number)
        if result == 'correct':
            print(f"Yeah! You gor it right in {attempt_number} guesses!")
            loop_control = False
        elif result == 'low':
            print(f"Your guess is too low.")
            attempt_number += 1
        else:
            print(f"Your guess is too high.")
            attempt_number += 1
    if attempt_number > 5:
        print(f"Sorry, you took 5 guesses and didn't get my number {target_number}!")

def play_game():
    """
    Function play_game()
    Parameters: nothing
    Returns: Initiates the guessing game
    """
    loop_control_game = True
    while loop_control_game:
        play_round()
        loop_control_game = ask_to_play_again()
    print("Thanks for playing!")

if __name__ =="__main__":
    pass