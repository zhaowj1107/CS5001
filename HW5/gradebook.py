"""
File: gradebook.py
Author: Weijian Zhao(David)
Date: 2025-02-13
Class: CS_5001, Spring_2025
Description: 
homework 5-2: Gradebook
"""


def find_student(students: list, name: str):
    """
    Finds a student dictionary by name in a list of student dictionaries.
    Parameters:
        students: list of student dictionaries
        name: string name to search for
    Returns:
        dictionary for matching student or None if not found
    >>> find_student([{'name': 'Alice'}, {'name': 'Bob'}], 'Alice')
    {'name': 'Alice'}
    >>> find_student([{'name': 'Alice'}, {'name': 'Bob'}], 'Charlie') is None
    True
    """
    for dict in students:
        if name == dict['name']:
            return dict
    return None


def get_average(numbers, drop_lowest: int = 0):  # include zero or not?
    """
    Calculates the average of a list of numbers
    optionally dropping the lowest scores.
    Parameters:
        numbers: list of numbers to average
        drop_lowest: number of lowest scores to drop (default 0)
    Returns:
        average of the numbers after dropping lowest scores
    >>> get_average([85, 90, 78, 92, 88], 0)
    86.6
    >>> get_average([85, 90, 78, 92, 88], 1)
    88.75
    >>> get_average([85, 90, 78, 92, 88], 2)
    90.0
    """
    numbers.sort(reverse=True) # sort the list in descending order
    while drop_lowest > 0:
        if numbers[-1] >= 0:
            numbers.pop()
        drop_lowest = drop_lowest - 1
    sum = 0
    for score in numbers:
        sum += score
    return sum / len(numbers)


def calculate_student_average(student: dict, grade_structure: dict):
    """
    Calculates a student's weighted average grade based on grade structure.
    Parameters:
        student: dictionary containing student's grades
        grade_structure: dictionary containing weights and drop rules
    Returns:
        weighted average grade as float
    >>> grade_structure = {
    ...     'homework': {'weight': 0.3, 'drop_lowest': 1},
    ...     'quizzes': {'weight': 0.2, 'drop_lowest': 1},
    ...     'midterm': {'weight': 0.2},
    ...     'final': {'weight': 0.3}
    ... }
    >>> student = {
    ...     'name': 'Alice',
    ...     'homework': [100, 100, 95],
    ...     'quizzes': [100, 80],
    ...     'midterm': 100,
    ...     'final': 100
    ... }
    >>> calculate_student_average(student, grade_structure)
    100.0
    >>> grade_structure1 = {
    ...     'homework': {'weight': 0.3, 'drop_lowest': 1},
    ...     'quizzes': {'weight': 0.2, 'drop_lowest': 0},
    ...     'midterm': {'weight': 0.2},
    ...     'final': {'weight': 0.3}
    ... }
    >>> student1 = {
    ...     'name': 'Alice',
    ...     'homework': [100, 100, 85],
    ...     'quizzes': [100, 0],
    ...     'midterm': 100,
    ...     'final': 100
    ... }
    >>> calculate_student_average(student1, grade_structure1)
    90.0
    """
    homework_avg = get_average(student['homework'], 
                               grade_structure['homework']['drop_lowest'])
    quizzes_avg = get_average(student['quizzes'], 
                              grade_structure['quizzes']['drop_lowest'])
    midterm_score = student['midterm']
    final_score = student['final']
    homework_avg_weight = homework_avg * grade_structure['homework']['weight']
    quizzes_avg_weight = quizzes_avg * grade_structure['quizzes']['weight']
    midterm_weight = midterm_score * grade_structure['midterm']['weight']
    final_weight = final_score * grade_structure['final']['weight']
    total_avg = homework_avg_weight + quizzes_avg_weight
    total_avg = total_avg + midterm_weight + final_weight
    return total_avg


def get_letter_grade(average_grade: float, grade_cutoffs: dict):
    """
    Converts a numeric grade to a letter grade based on cutoff scores.
    Parameters:
        average_grade: float representing the student's average grade
        grade_cutoffs: dictionary mapping letter grades to minimum scores
    Returns:
        string representing the letter grade
    >>> grade_cutoffs = {'A+': 95, 'A': 90, 'B+': 85, 'B': 80, 'C+': 75}
    >>> get_letter_grade(97, grade_cutoffs)
    'A+'
    >>> get_letter_grade(83, grade_cutoffs)
    'B'
    >>> get_letter_grade(76.5, grade_cutoffs)
    'C+'
    >>> get_letter_grade(90, grade_cutoffs)
    'A'
    >>> get_letter_grade(70, grade_cutoffs)
    'Invalid Score'
    """
    # if dictionary is not in order, how could we know that 
    # the iteration will go from first to last
    final_letter = ""
    for letter, score in grade_cutoffs.items(): # in python 3.7 above, dictionary is ordered
        if average_grade >= score:
            return letter
    return 'Invalid Score'


def display_student_report(student: dict, grade_structure: dict, 
                           grade_cutoffs: dict):

    average_grade = calculate_student_average(student, grade_structure)
    letter = get_letter_grade(average_grade, grade_cutoffs)
    print(f"{student['name']}: {round(average_grade, 1)}% ({letter})")
    return None


def display_class_report(students: list, grade_structure: dict, 
                         grade_cutoffs: dict):
    for student_index in range(len(students)):
        display_student_report(students[student_index], 
                               grade_structure, grade_cutoffs)
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
