'''
CS5001
Homework 3
Spring 2025
Yi Han
'''

from rps_functions import (
    get_computer_choice,
    get_user_choice,
    beats,
    play_round,
    is_positive_integer,
    play_game
)


def main():
    num_rounds = is_positive_integer()
    round_numbers = num_rounds
    user_rock = user_paper = user_scissors = 0
    computer_rock = computer_paper = computer_scissors = 0
    wins = losses = draws = 0
    title = 1

    while round_numbers > 0:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(f"\nRound {title}")
        print(f"You choose: {user_choice}")
        print(f"Computer choose: {computer_choice}")

        result = play_round(user_choice, computer_choice)
        if result == 'win':
            print("You won this round!\n")
            wins += 1
        elif result == 'lost':
            print("You lost this round!\n")
            losses += 1
        else:
            print("This round is a draw!\n")
            draws += 1

        if user_choice == "Rock":
            user_rock += 1
        elif user_choice == "Paper":
            user_paper += 1
        else:  # user_choice == "Scissors"
            user_scissors += 1

        if computer_choice == "Rock":
            computer_rock += 1
        elif computer_choice == "Paper":
            computer_paper += 1
        else:  # computer_choice == "Scissors"
            computer_scissors += 1

        round_numbers -= 1
        title += 1

    play_game(
        num_rounds,
        wins,
        losses,
        draws,
        user_rock,
        user_paper,
        user_scissors,
        computer_rock,
        computer_paper,
        computer_scissors
    )


if __name__ == "__main__":
    import doctest
    import rps_functions
    doctest.testmod(rps_functions, verbose=True)

    main()
