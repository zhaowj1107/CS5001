"""
File: parks_functions.py
Author: Weijian Zhao(David)
Date: 2025-02-24
Class: CS_5001, Spring_2025
Description: 
homework 6: Parks and Neighbourhoods
"""

import requests


def read_from_file(filename: str) -> list[str]:
    '''
    Function read_from_file()
    Parameters: filename (str) - name of file to read from
    Returns: list[str] - list of strings containing file contents
    Reads contents from a file and returns as list of strings.
    Handles file not found and permission errors.
    '''
    list_1 = []
    try:
        file_path = "Project/CS5001/HW6/"
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
    return list_1


def read_from_url(url: str) -> list[str]:
    """
    Function read_from_url()
    Parameters:
        url (str): The URL of the text file to be read.
    Returns:
        list[str]: A list of strings, where each string represents a line from the text file.
    Description:
        This function fetches the content of a text file from the given URL and returns its contents
        as a list of lines. It handles potential errors such as connection issues and unexpected 
        failures.
    Error Handling:
        - Prints an error message if a request fails due to network issues, invalid URL, or other exceptions.
        - Returns an empty list if an error occurs.
    """
    try:
        resp = requests.get(url)  # get the response from the website
        list_1 = resp.text.splitlines()
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        return list_1


def construct_park_dictionary(contents: list[str]) -> dict[str, list]:
    '''
    Function construct_park_dictionary()
    Parameters: contents (list[str]) - list of strings containing park data
    Returns: dict[str, list] - dictionary mapping park names to neighbourhoods
    Constructs a dictionary from park data where keys are park names
    and values are lists containing neighbourhood information.
    >>> data = [
    ...     "Park Name,Neighbourhood",
    ...     "Green Park,Midtown",
    ...     "Blue Park,Midtown",
    ...     "Sunny Park,Midtown",
    ... ]
    >>> construct_park_dictionary(data)
    {'Midtown': ['Green Park', 'Blue Park', 'Sunny Park']}
    >>> construct_park_dictionary(["Park Name,Neighbourhood"])  # No parks, only header
    {}
    >>> construct_park_dictionary([])  # Empty list
    {}
    '''
    try:
        neighbourhood_parks = {}
        for line in contents[1:]:  # Start reading from the second line
            if not line.strip():  # Ignore empty lines
                continue
            park_name, neighbourhood = line.strip().split(",", 1)  # Only split at the first comma
            park_name, neighbourhood = park_name.strip(), neighbourhood.strip()
            if neighbourhood not in neighbourhood_parks:
                neighbourhood_parks[neighbourhood] = []
            neighbourhood_parks[neighbourhood].append(park_name)
        return neighbourhood_parks
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_parks_in_neighbourhood(parks: dict[str, list[str]], neighbourhood: str) -> list[str]:
    """
    Function get_parks_in_neighbourhood()
    Parameters:
        parks (dict[str, list[str]]) - Dictionary where keys are park names 
                                       and values are lists of neighbourhoods.
        neighbourhood (str) - The neighbourhood to search for parks in.
    Returns:
        list[str] - List of parks in the given neighbourhood.

    Handles:
    - Invalid input types
    - Missing neighbourhoods
    - Unexpected data format issues
    >>> parks_dict = {
    ...     "Downtown": ["Central Park", "Sunset Park"],
    ...     "Uptown": ["Riverside Park"],
    ...     "Suburbia": ["Hilltop Park", "Green Meadow"]
    ... }
    >>> get_parks_in_neighbourhood(parks_dict, "Downtown")
    ['Central Park', 'Sunset Park']
    >>> get_parks_in_neighbourhood(parks_dict, "Uptown")
    ['Riverside Park']
    """
    try:
        if not isinstance(parks, dict):
            raise TypeError("Invalid input: parks must be a dictionary.")
        if not isinstance(neighbourhood, str):
            raise TypeError("Invalid input: neighbourhood must be a str.")

        return parks.get(neighbourhood, [])  # Returns the list of parks or an empty list if the neighbourhood is missing

    except TypeError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def count_neighbourhood_parks(parks: dict[str, list[str]]) -> dict[str, int]:
    """
    Function count_neighbourhood_parks()
    Parameters: parks (dict[str, list[str]]) - dictionary mapping park names to neighbourhoods
    Returns: dict[str, int] - dictionary mapping neighbourhood names to park counts
    Counts the number of parks in each neighbourhood and returns a dictionary with the counts.
    Examples:
    >>> parks_dict = {
    ...     "Downtown": ["Central Park", "Sunset Park"],
    ...     "Uptown": ["Riverside Park"],
    ...     "Suburbia": ["Hilltop Park", "Green Meadow", "Lakeside Park"]
    ... }
    >>> count_neighbourhood_parks(parks_dict)
    {'Downtown': 2, 'Uptown': 1, 'Suburbia': 3}

    >>> count_neighbourhood_parks({})
    {}
    """
    try:
        if not isinstance(parks, dict):
            raise TypeError("Invalid input: parks must be a dictionary.")

        # Ensure all values in the dictionary are lists
        for neighbourhood, park_list in parks.items():
            if not isinstance(park_list, list):
                raise ValueError(f"Invalid data format: parks in {neighbourhood} should be a list.")
        dict_count = {}
        for neigh, parks_list in parks.items():
            dict_count[neigh] = len(parks_list)
        return dict_count
    except TypeError as e:
        print(f"Error: {e}")
        return {}
    except ValueError as e:
        print(f"Error: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


def get_neighbourhood_with_most_parks(parks: dict[str, str]) -> str:
    """
    Returns the neighbourhood with the most parks from the given parks dictionary.
    If there's a tie, returns the neighbourhood that comes first alphabetically.
    Examples:
    >>> parks_dict = {
    ...     "Downtown": ["Central Park", "Sunset Park"],
    ...     "Uptown": ["Riverside Park"],
    ...     "Aptown": ["Sunrise Park", "Sunset Park"]
    ... }
    >>> get_neighbourhood_with_most_parks(parks_dict)
    'Aptown'
    >>> parks_dict = {
    ...     "Downtown": ["Central Park", "Sunset Park"],
    ...     "Uptown": ["Riverside Park"],
    ...     "Suburbia": ["Hilltop Park", "Green Meadow", "Lakeside Park"]
    ... }
    >>> get_neighbourhood_with_most_parks(parks_dict)
    'Suburbia'
    """
    try:
        if not isinstance(parks, dict):  # Ensure input is a dictionary
            raise TypeError("Invalid input: parks must be a dictionary.")
        dict_count = count_neighbourhood_parks(parks)
        if not dict_count:  # Handle case where no parks exist
            raise ValueError("No parks found in the provided dictionary.")
        holder = -1
        result = None
        for neigh, number in dict_count.items():
            if not isinstance(neigh, str) or not isinstance(number, int):
                raise ValueError(f"Invalid data format: '{neigh}': {number}")

            if number > holder:
                holder = number
                result = neigh
            elif number == holder:
                if result is not None and result.lower() > neigh.lower():
                    result = neigh

        if result is None:
            raise ValueError("Unable to determine the neighbourhood with the most parks.")

        return result
    except KeyError as e:
        print(f"Error: Missing expected key in dictionary - {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
