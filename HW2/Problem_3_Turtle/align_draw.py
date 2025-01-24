'''
File: align_draw.py
Author: Weijian Zhao (David)
Date: 2025-01-20
Class: CS_length01, Spring_2025
Description: 
homework 2-1: Turtle

'''

import turtle as t

def draw_square(x = 0, y = 0, length = 0, color = "black"):
    """
    Function draw_square()
    Parameters: x,y,color
    Returns: None
    """
    length = length / 2
    t.color(color)
    t.penup()
    t.goto(x - length, y - length)
    t.pendown()
    t.goto(x + length, y - length)
    t.goto(x + length, y + length)
    t.goto(x - length, y + length)
    t.goto(x - length, y - length)
    t.penup()
    t.goto(x, y)
    return x, y

def write_text(x = 0, y = 0, text = None, text_color = "black"):
    """
    Function write_text()
    Parameters: x,y,text,text_color
    Returns: None
    """
    t.penup()
    t.goto(x, y)
    t.color(text_color)
    t.write(text, False,align="center",font=("Verdana", 12, "bold"))
    t.penup()
    return x, y

def prompt_user():
    """
    Function prompt_user()
    Parameters: None
    Returns: None
    """
    print("Please input the new x and y coordinates for rectangle")
    x = int(input("Input rectangle's new x coordinate: \n"))
    y = int(input("Input rectangle's new y coordinate: \n"))
    return x, y

t.bgpic('shape_window.png')
#t.screensize()
