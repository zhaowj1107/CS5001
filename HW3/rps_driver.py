"""
File: rps_driver
Author: Weijian Zhao (David)
Date: 2025-01-27
Class: CS_5001, Spring_2025
Description: 
homework 2-1: Rock, Paper, Scissors
"""
import rps_functions as rpsf


def main():
    """
    Function main()
    Parameters: nothing
    Returns: None
    description: driver file and main function
    """
    rpsf.play_game()


if __name__ == "__main__":
    import doctest
    doctest.testmod(rpsf, verbose=True)
    main()
