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


def get_average(numbers, drop_lowest: int = 0): # greater than zero include zero or not?
    """
    Calculates the average of a list of numbers, optionally dropping the lowest scores.
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
    numbers.sort(reverse=True)
    while drop_lowest > 0:
        if numbers[-1] >= 0 :
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
    homework_avg = get_average(student['homework'], grade_structure['homework']['drop_lowest'])
    quizzes_avg = get_average(student['quizzes'], grade_structure['quizzes']['drop_lowest'])
    midterm_score = student['midterm']
    final_score = student['final']
    homework_avg_weight = homework_avg * grade_structure['homework']['weight']
    quizzes_avg_weight = quizzes_avg * grade_structure['quizzes']['weight']
    midterm_weight = midterm_score * grade_structure['midterm']['weight']
    final_weight = final_score * grade_structure['final']['weight']
    total_avg = homework_avg_weight + quizzes_avg_weight + midterm_weight + final_weight
    return total_avg

def get_letter_grade(average_grade: float, grade_cutoffs: dict):

    # if dictionary is not in order, how could we know it the iteration will go from first to last
    final_letter = ""
    for letter, score in grade_cutoffs.items():
        if average_grade >= score:
            return letter
    return 'Invalid Score'


def display_student_report(student: dict, grade_structure: dict, grade_cutoffs: dict):

    average_grade = calculate_student_average(student, grade_structure)
    letter = get_letter_grade(average_grade, grade_cutoffs)
    print(f"{student['name']}: {round(average_grade, 1)}% ({letter})")
    return None

def display_class_report(students: list, grade_structure: dict, grade_cutoffs: dict):
    for student_index in range(len(students)):
        display_student_report(students[student_index], grade_structure, grade_cutoffs)
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    from student_data import STUDENTS
    from grade_cutoffs import GRADE_CUTOFFS
    from grade_structure import GRADE_STRUCTURE
    # test_scores = [85, 90, 78, 92, 88]
    # print("Lowest score:", find_lowest(test_scores))  # Should print 78

    # print("Average with no drop:", get_average(test_scores))  # Should print 86.6
    # print("Average with drop lowest:", get_average(test_scores, 78))  # Should print 88.75

    # first_student = STUDENTS[0]
    # avg = calculate_student_average(first_student, GRADE_STRUCTURE)
    # print(f"{first_student['name']} average:", avg)

    # print("A+ grade:", get_letter_grade(97, GRADE_CUTOFFS))  # Should print A+
    # print("B grade:", get_letter_grade(83, GRADE_CUTOFFS))   # Should print B
    # print("F grade:", get_letter_grade(59, GRADE_CUTOFFS))   # Should print F

    # display_student_report(first_student, GRADE_STRUCTURE, GRADE_CUTOFFS) # Test display_student_report

    # display_class_report(STUDENTS, GRADE_STRUCTURE, GRADE_CUTOFFS) # Test display_class_report
    # display_student_report("Alice Smith", GRADE_STRUCTURE, GRADE_CUTOFFS)