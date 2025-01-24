'''
File: align_draw_deriver.py
Author: Weijian Zhao (David)
Date: 2025-01-20
Class: CS_5001, Spring_2025
Description: 
homework 2-1: Turtle

'''
import turtle as t
import align_draw as ad
import time

def main():
    SQUARE_LENGTH = 150
    # Set up the screen with a background image
    screen = t.Screen()
    screen.bgpic('shape_window.png')
    screen.screensize(970,637)
    x, y = 0, 0

    # Draw a square and write text
    square_x, square_y = ad.draw_square(x, y, SQUARE_LENGTH, "red")
    word_x, word_y = ad.write_text(x, y, "hello world", "blue")

    # Prompt the user for new coordinates
    x,y = ad.prompt_user()

    # earse the previous square and text
    word_x, word_y = ad.write_text(word_x, word_y, "hello world", "white")
    # t.undo()
    square_x, square_y = ad.draw_square(square_x, square_y, SQUARE_LENGTH, "white")

    # Draw a square and write text with new coordinates
    ad.draw_square(x, y, SQUARE_LENGTH, "blue")
    ad.write_text(x, y, "hello world", "red")


if __name__ == "__main__":
    main()
    # Keep the window open
    time.sleep(10000)