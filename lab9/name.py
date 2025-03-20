"""
File: name.py
Author:  Weijian Zhao (David)
Date: 2025-03-12
Class: CS_5001, Spring_2025
"""


class Name:
    def __init__(self, first_name, last_name):
        """
        Constructor
        :param first_name: str, the first name
        :param last_name: str, the last name
        """
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("First name and last name must be strings.")
        if (" " in first_name) or (" " in last_name):
            raise ValueError("First name and last name =contain spaces.")
        condition1 = any(not c.isalpha() for c in first_name)
        condition2 = any(not c.isalpha() for c in last_name)
        if condition1 or condition2:
            raise ValueError("Name cannot contain special characters.")
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty.")
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = first_name

    def get_first_name(self):
        """
        Returns the first name of the person
        :return: str, the first name
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns the last name of the person
        :return: str, the last name
        """
        return self.last_name

    def get_full_name(self):
        """
        Returns the full name of the person
        :return: str, the full name
        """
        return self.first_name + " " + self.last_name

    def set_nick_name(self, nick_name):
        """
        Sets the nickname of the person
        :param nick_name: str, the nickname
        """
        if not isinstance(nick_name, str):
            raise TypeError("Nickname must be a string.")
        if (" " in nick_name):
            raise ValueError("Nick name cannot contain spaces.")
        if any(not c.isalpha() for c in nick_name):
            raise ValueError("Name cannot contain special characters.")
        if not nick_name:
            raise ValueError("Nickname cannot be empty.")
        self.nick_name = nick_name

    def get_nick_name(self):
        """
        Returns the nickname of the person
        :return: str, the nickname
        """
        return self.nick_name

    def __str__(self):
        """
        Returns a formatted string representing the person's full name
        :return: str, the formatted string
        """
        return f"{self.first_name} \"{self.nick_name}\" {self.last_name}"

    def __eq__(self, other):
        """
        Compares two Name objects for equality based on their full names.
        """
        if not isinstance(other, Name):
            raise TypeError("Comparing object must be of type Name.")
        first_tell = self.first_name == other.first_name
        last_tell = self.last_name == other.last_name
        return first_tell and last_tell


if __name__ == "__main__":  # pragma: no cover
    name1 = Name("Joseph", "Schmeggeggie")
    name2 = Name("Joseph", "Schmeg")
