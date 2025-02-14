"""
File: gradebook.py
Author: Weijian Zhao(David)
Date: 2025-02-13
Class: CS_5001, Spring_2025
Description: 
homework 5-2: Gradebook
"""


from student_data import STUDENTS

def find_student(students: list, name: str):

    for dict in students:
        if name == dict['name']:
            return dict
        else:
            return None


def get_average(numbers, drop_lowest: int = 0):
    if drop_lowest > 0 :
        numbers.remove(drop_lowest)
    sum = 0
    for score in numbers:
        sum =+ score
    return sum / len(numbers)


def calculate_student_average

print(find_student(STUDENTS, "Alice Smith"))