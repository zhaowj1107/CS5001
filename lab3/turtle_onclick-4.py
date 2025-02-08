import turtle

'''
    Event-driven programming introduction:
'''

def get_click(x, y):
    print("I caught you clicking at ({}, {})!".format(x, y))
    if x > 100:
        print("high x!")

def draw_square(x = 0, y = 0, length = 100, color = "black"):
    """
    Function draw_square()
    Parameters: x,y,color
    Returns: None
    >>> draw_square(0, 0, 150, "black")
    (0, 0)
    >>> draw_square(150, 150, 150, "red")
    (150, 150)
    """
    length = int(length) / 2
    turtle.color(color)
    turtle.penup()
    turtle.goto(x - length, y - length)
    turtle.pendown()
    turtle.goto(x + length, y - length)
    turtle.goto(x + length, y + length)
    turtle.goto(x - length, y + length)
    turtle.goto(x - length, y - length)
    turtle.penup()
    turtle.goto(x, y)
    return x, y

def main():
    tommy = turtle.Turtle() # create our turtle
    screen = turtle.Screen() # get a screen variable
    
    # screen.onclick(draw_square) # register your event handler
    screen.onclick(turtle.goto) # register your event handler
    
    tommy.circle(100) # draw a circle using the turtle
    
    # The turtle event loop continues from here, sort of like a
    # while True: until we exit the program
    # it turns get_click into a sort of main program that runs every time
    # that there is a click
    

if __name__ == "__main__":
    main()
    turtle.done() # keep the window open