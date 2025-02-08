import turtle
from PositionService import get_position_x, get_position_y, record_position, \
    change_status_of_set_position, check_if_position_is_set, record_position_x, \
        record_position_y

'''
    Event-driven programming introduction: 
'''

def draw_square(tommy):
    tommy.right(90)
    tommy.forward(90)

    tommy.right(90) 
    tommy.forward(90)

    tommy.right(90)
    tommy.forward(90)

    tommy.right(90)
    tommy.forward(90)

def get_click(x, y):
    # global click_counter
    if check_if_position_is_set() is False:
        print("First click! You clicked at ({}, {})\n".format(x, y))
        record_position(x, y)
        change_status_of_set_position(True)
    else:
        x_last = get_position_x()
        y_last = get_position_y()
        print("you clicked at ({}, {}) click! last click was at ({}, {})\n".format(x, y, x_last, y_last))
        if y > y_last:
            print("this y was greater!\n")
        else:
            print("last click's y was greater!\n")
        record_position(x, y)
        change_status_of_set_position(True)


def main():
    #click_counter = 0
    tommy = turtle.Turtle() # create our turtle
    screen = turtle.Screen() # get a screen variable
    screen.onclick(get_click) # register your event handler

    draw_square(tommy) #draw a circle using the turtle
    
    # The turtle event loop continues from here, sort of like a
    # while True: until we exit the program
    # it turns get_click into a sort of main program that runs every time
    # that there is a click
    

if __name__ == "__main__":
    main()
    turtle.done() # keep the window open