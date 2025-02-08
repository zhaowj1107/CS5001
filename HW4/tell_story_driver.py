"""
File: tell_story_driver.py
Author: Weijian Zhao (David)
Date: 2025-02-03
Class: CS_5001, Spring_2025
Description: 
homework 4-3: Tell Me a Story
"""
import tell_story as ts


def main():
    """
    Function main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    story_list = [
        "Once upon a time in a place called Align, a curious student named Sara enrolled in CS 5001.",
        "Sara had always been fascinated by technology, but coding was a new world to her.",
        "The first day, she was introduced to Python. \"It's like magic,\" the professor said with a twinkle in her eye.",
        "Every day, Sara would write lines of code, turning thoughts into actions on the screen.",
        "Sometimes she got stuck. But with each challenge, she learned to think differently.",
        "She made friends in the class, and they would solve problems together, late into the night.",
        "By the end of the semester, Sara had built her very first program.",
        "Proud and amazed, she realized that with Python, she could make computers dance to her tune.",
        "And so, under the starry sky of Align, Sara drifted into dreams of endless possibilities."
    ]
    direction = input("Enter the direction (forward, backward, every other): ")
    End = input("Enter the ending (stars, sun, anything else): ")
    print(ts.generate_story(story_list, direction, End))


if __name__ == "__main__":
    main()
