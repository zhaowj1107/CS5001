"""
File: rps_functions
Author: Weijian Zhao (David)
Date: 2025-01-27
Class: CS_5001, Spring_2025
Description: 
homework 2-1: Rock, Paper, Scissors
"""
import random

def get_computer_choice():
    """
    Function generate_target()
    Parameters: nothing
    Returns: randome str value
    >>> choice = get_computer_choice()
    >>> choice == "Rock" or choice == "Paper" or choice == "Scissors"
    True
    """
    random_number = random.randint(1, 3)
    if random_number == 1:
        return "Rock"
    elif random_number == 2:
        return "Paper"
    else:
        return "Scissors"


def get_user_choice():
    """
    Function get_user_choice()
    Parameters: nothing
    Returns: str value
    """
    user_input = int(input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))
    while not (user_input==1 or user_input==2 or user_input==3):
        print("Invalid input number. Please try again")
        user_input = int(input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))
    if user_input == 1:
        return "Rock"
    elif user_input == 2:
        return "Paper"
    else:
        return "Scissors"


def beats(user_choice: str, computer_choice: str):
    """
    Function get_user_choice()
    Parameters: two string
    Returns: str value
    >>> beats("Rock", "Scissors")
    True
    >>> beats("Scissors", "Rock")
    False
    >>> beats("Paper", "Rock")
    True
    >>> beats("Rock", "Paper")
    False
    >>> beats("Scissors", "Paper")
    True
    >>> beats("Paper", "Scissors")
    False
    >>> beats("Rock", "Rock")
    False
    >>> beats("Paper", "Paper")
    False
    >>> beats("Scissors", "Scissors")
    False
    """
    rock = "Rock"
    paper = "Paper" 
    scissors = "Scissors"
    if user_choice == rock:
        if computer_choice == paper:
            return False
        elif computer_choice == scissors:
            return True
        else:
            return False
    elif user_choice == paper:
        if computer_choice == scissors:
            return False
        elif computer_choice == rock:
            return True
        else:
            return False
    else:
        if computer_choice == rock:
            return False
        elif computer_choice == paper:
            return True
        else:
            return False


def play_round():
    """
    Function is_positive_integer()
    Parameters: Nothing
    Returns: three strs
    print out the result of one round
    """
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    game_result = beats(user_choice, computer_choice)
    if game_result == True:
        print("You won this round!\n")
        return computer_choice, user_choice, "win" # How could I write the log if I did not return the varibales during the game
    else:
        if computer_choice == user_choice:
            print("This round is a draw!\n")
            return computer_choice, user_choice, "draw"
        else:
            print("You lost this round!\n")
            return computer_choice, user_choice, "loss"


def is_positive_integer():
    """
    Function is_positive_integer()
    Parameters: nothing
    Returns: int
    Prompts the user for a valid positive integer input (number of rounds).
    """
    round_num = int(input('Enter the number of rounds to play: '))
    while round_num < 1:
        print("Invalid input number. Please try again\n")
        round_num = int(input('Enter the number of rounds to play: '))
    return round_num

def play_game():
    """
    Function is_positive_integer()
    Parameters: nothing
    Returns: int
    description:
    Manages the game for a specified number of rounds, 
    keeps track of wins/losses, and displays the statistics.
    """
    round_num = is_positive_integer()
    round_num_loop = round_num
    win, loss, draw = 0, 0, 0
    user_rock, user_paper, user_scissors = 0, 0, 0
    computer_rock, computer_paper, computer_scissors = 0, 0, 0
    while round_num_loop > 0:
        user_choice, computer_choice, result = play_round()
        round_num_loop -= 1
        #count the result of game
        if result == "win":
            win += 1
        elif result == "loss":
            loss += 1
        else:
            draw += 1
        #count the input of user
        if user_choice == "Rock":
            user_rock += 1
        elif result == "Paper":
            user_paper += 1
        else:
            user_scissors += 1
        #count the input of user
        if computer_choice == "Rock":
            computer_rock += 1
        elif computer_choice == "Paper":
            computer_paper += 1
        else:
            computer_scissors += 1

    #Print out the result of game
    print("Gmae Over!")
    print(f"Total Rounds: {round_num}")
    print(f"You won {win} times ({round(win/round_num*100, 1)}%).")
    print(f"The computer won {loss} times ({round(loss/round_num*100, 1)}%).")
    print(f"There were {draw} draws ({round(draw/round_num*100, 1)}%).\n")

    # Print out the process
    print("Choices:")
    print(f"You choices - Rock: {user_rock} Paper: {user_paper} Scissors: {user_scissors}")
    print(f"Computer choices - Rock: {computer_rock} Paper: {computer_paper} Scissors: {computer_scissors}\n")

    if win > loss:
        print("You are the overall winnder!")
    elif win < loss:
        print("The computer is the overall winnder!")
    else:
        print("This game is a draw overall!")


if __name__ == "__main__":
    pass