"""
File: gradebook_driver.py
Author: Weijian Zhao(David)
Date: 2025-02-13
Class: CS_5001, Spring_2025
Description: 
homework 5-2: Gradebook
"""


from student_data import STUDENTS
from grade_cutoffs import GRADE_CUTOFFS
from grade_structure import GRADE_STRUCTURE
import gradebook as g


def main():
    """
    Function: main
    Parameters: None
    Returns: Nothing
    Pring out the result
    """
    user_input = input("Do you wish to view reports for single\
student or whole class? (class/student) ")
    if user_input.lower() == "class":
        g.display_class_report(STUDENTS, GRADE_STRUCTURE, GRADE_CUTOFFS)
    elif user_input.lower() == "student":
        user_input2 = input("Which student would you like \
to view report? ")
        if g.find_student(STUDENTS, user_input2):
            student_dict = g.find_student(STUDENTS, user_input2)
            g.display_student_report(student_dict, 
                                     GRADE_STRUCTURE, GRADE_CUTOFFS)
        else:
            print(f"Cannot find student with name {user_input2}")
    else:
        return None


if __name__ == "__main__":
    main()
