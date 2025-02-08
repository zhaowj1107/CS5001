'''
    CS5001
    Homework 3
    Spring 2025
    Yi Han
'''
import random


def get_computer_choice() -> str:
    """
    Function: get_computer_choice()
    Parameters: no
    Return: random.choice ex: "Rock", "Paper", "Scissors"
    >>> choice = get_computer_choice()
    >>> choice in ("Rock", "Paper", "Scissors")
    True
    """
    return random.choice(("Rock", "Paper", "Scissors"))


def get_user_choice() -> str:
    """
    Function: get_computer_choice()
    Parameters: no
    Return: "Rock", "Paper", "Scissors"
    """
    user_choice = int(input("Enter 1 for Rock, 2 for Paper, or "
                            "3 for Scissors: "))
    while user_choice < 1 or user_choice > 3:
        print("Invalid input. Please try again.")
        user_choice = int(input("Enter 1 for Rock, "
                                "2 for Paper, or 3 for Scissors: "))
    if user_choice == 1:
        return 'Rock'
    elif user_choice == 2:
        return 'Paper'
    elif user_choice == 3:
        return 'Scissors'


def beats(user_choice: str, computer_choice: str) -> bool:
    """
    Function: beats()
    Parameters: user_choice: str, computer_choice: str
    Return: True or False
    >>> beats("Rock", "Scissors")
    True
    >>> beats("Rock", "Paper")
    False
    >>> beats("Paper", "Rock")
    True
    >>> beats("Paper", "Scissors")
    False
    >>> beats("Scissors", "Paper")
    True
    >>> beats("Scissors", "Rock")
    False
    >>> beats("Rock", "Rock")
    False
    >>> beats("Paper", "Paper")
    False
    >>> beats("Scissors", "Scissors")
    False
    """
    if user_choice == "Rock" and computer_choice == "Scissors":
        return True
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return True
    elif user_choice == "Paper" and computer_choice == "Rock":
        return True
    else:
        return False


def play_round(user_choice: str, computer_choice: str) -> str:
    """
    Function: get_computer_choice()
    Parameters: user_choice: str, computer_choice: str
    Return: "draw", "win", "lost"
    """
    if user_choice == computer_choice:
        return "draw"
    elif beats(get_user_choice, computer_choice):
        return "win"
    else:
        return "lost"


def is_positive_integer() -> int:

    """
    Function: is_positive_integer()
    Parameters: 0
    Return: rounds
    """
    rounds = int(input("Enter the number of rounds to play: "))
    return rounds


def play_game(
    total_rounds: int = 0,
    wins: int = 0, 
    losses: int = 0, 
    draws: int = 0,
    user_rock: int = 0, 
    user_paper: int = 0, 
    user_scissors: int = 0,
    computer_rock: int = 0,
    computer_paper: int = 0,
    computer_scissors: int = 0
) -> None:
    """
    Function: play_game() Manages the game for a specified number of rounds
    Parameters: total_rounds: int,
    wins: int, 
    losses: int, 
    draws: int,
    user_rock: int, 
    user_paper: int, 
    user_scissors: int,
    computer_rock: int,
    computer_paper: int,
    computer_scissors: int
    Return: no
    """
    if total_rounds > 0:
        win_percentage = (wins / total_rounds) * 100
        loss_percentage = (losses / total_rounds) * 100
        draw_percentage = (draws / total_rounds) * 100
    else:
        win_percentage = loss_percentage = draw_percentage = 0.0
    print("\nGame Over!")
    print(f"Total Rounds: {total_rounds}")
    print(f"You won {wins} times ({win_percentage:.1f}%).")
    print(f"The computer won {losses} times ({loss_percentage:.1f}%).")
    print(f"There were {draws} draws ({draw_percentage:.1f}%).")

    # Print how many times each choice was made
    print("\nChoice Statistics:")
    print(f"Your choices -> Rock: {user_rock}, "
          "Paper: {user_paper}, Scissors: {user_scissors}")
    print(f"Computer choices -> Rock: {computer_rock}, "
          "Paper: {computer_paper}, Scissors: {computer_scissors}")

    # Determine overall winner
    if wins > losses:
        print("\nYou are the overall winner!")
    elif losses > wins:
        print("\nThe computer is the overall winner!")
    else:
        print("\nIt's an overall tie! Well played!")


if __name__ == "__main__":
    import doctest
    import rps_functions
    doctest.testmod(rps_functions, verbose=True)   
