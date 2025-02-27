'''
File: parkiest_neighbourhood_functions.py
Author:  Weijian Zhao (David)
Date: 2025-02-19
Class: CS_5001, Spring_2025
'''


def read_from_file(filename: str = "parks_name_neighbourhood.txt"):
    '''
    Function read_from_file()
    Parameters: filename (str) - name of file to read from
    Returns: list[str] - list of strings containing file contents
    Reads contents from a file and returns as list of strings.
    Handles file not found and permission errors.
    '''
    list_1 = []
    list_park = []
    list_neigh = []
    try:
        file_path = "Project/CS5001/lab7/"
        with open(filename, "r") as file:
            for line in file:
                list_1.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except IOError:
        print(f"Error: An I/O error occurred while accessing '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")

    try:
        for line in list_1[1:]:  # Start reading from the second line
            if not line.strip():  # Ignore empty lines
                continue
            park_name, neighbourhood = line.strip().split(",", 1)
            park_name, neighbourhood = park_name.strip(), neighbourhood.strip()
            list_park.append(park_name)
            list_neigh.append(neighbourhood)
        return list_park, list_neigh
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def construct_park_dictionary(list_park: list[str], list_neigh: list[str]):
    '''
    Function construct_park_dictionary()
    Parameters: contents (list[str]) - list of strings containing park data
    Returns: dict[str, list] - dictionary mapping park names to neighbourhoods
    Constructs a dictionary from park data where keys are park names
    and values are lists containing neighbourhood information.
    '''
    neighbourhood_parks = {}
    if not isinstance(list_park, list):
        raise TypeError("Invalid input: list_park must be a list.")
    if not isinstance(list_neigh, list):
        raise TypeError("given lists of different lengths")
    if len(list_park) != len(list_neigh):
        raise ValueError("Given lists of different lengths")
    for index in range(len(list_park)):
        if list_neigh[index] not in neighbourhood_parks:
            neighbourhood_parks[list_neigh[index]] = []
        neighbourhood_parks[list_neigh[index]].append(list_park[index])
    return neighbourhood_parks


def display_parks_and_neighbourhood(dict_park):
    '''
    Function: display_parks_and_neighbourhood
    Parameters: dict_park (dict) - dictionary mapping neighbourhoods
    Returns: None
    Displays all parks and their corresponding neighbourhoods
    the input dictionary and printing formatted output showing each park
    '''
    if not isinstance(dict_park, dict):
        raise TypeError("Invalid input: dict_park must be a dict.")
    for neigh in dict_park.keys():
        for park in dict_park[neigh]:
            print(f"{park} in {neigh}")


def count_neighbourhood_parks(dict_park):
    '''
    Function: count_neighbourhood_parks
    Parameters: dict_park (dict) - dictionary mapping neighbourhoods
    Returns: dict - dictionary mapping neighbourhoods to their park counts
    Counts the number of parks in each neighbourhood by iterating through
    the input dictionary and creating a new dictionary with counts
    '''
    dict_park_count = {}
    if not isinstance(dict_park, dict):
        raise TypeError("Invalid input: dict_park must be a dict.")
    for neigh in dict_park.keys():
        dict_park_count[neigh] = len(dict_park[neigh])
    return dict_park_count


def display_parks_per_neighbourhood(dict_park_count):
    '''
    Function: display_parks_per_neighbourhood
    Parameters: dict_park_count (dict) - dictionary mapping neighbourhoods
    Returns: dict - the input dictionary is returned unchanged
    Displays the number of parks in each neighbourhood by iterating through
    the dictionary and printing formatted output
    '''
    if not isinstance(dict_park_count, dict):
        raise TypeError("Invalid input: dict_park must be a dict.")
    for niegh_for_count, number in dict_park_count.items():
        # if not isinstance(niegh_for_count, str):
        #     raise TypeError("Invalid input: niegh_for_count must be a str.")
        # if not isinstance(number, int):
        #     raise TypeError("Invalid input: number must be a int.")
        print(f"There are {number} parks in {niegh_for_count}")
    return dict_park_count


if __name__ == "__main__":
    # dict_park_count = {2: 2, 3: 2}
    # display_parks_per_neighbourhood(dict_park_count)
    pass
