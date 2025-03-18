"""
File: test_notebook_pytest.py
Author: Weijian Zhao(David)
Date: 2025-03-18
Class: CS_5001, Spring_2025
Description: 
homework 7: test_Shapes
"""
import os
import pytest
import tempfile
from notebook import Notebook


def test_constructor():
    """
    Test the constructor
    """
    n = Notebook()
    assert n.notes == []


def test_add_note():
    """
    Test the add_note method
    """
    n = Notebook()
    n.add_note("Hello world")
    assert n.notes == ["Hello world"]


def test_add_note_error():
    """
    Test the add_note method with invalid input
    """
    n = Notebook()
    with pytest.raises(TypeError):
        n.add_note(5)


def test_get_note():
    """
    Test the get_note method
    """
    n = Notebook()
    n.add_note("Hello world")
    assert n.get_note(0) == "Hello world"


def test_get_note_error():
    """
    Test the get_note method with invalid input
    """
    n = Notebook()
    with pytest.raises(IndexError):
        n.get_note(0)


def test_get_note_error2():
    """
    Test the get_note method with invalid input
    """
    n = Notebook()
    n.add_note("Hello world")
    with pytest.raises(IndexError):
        n.get_note(3)


def test_total_notes():
    """
    Test the total_notes method
    """
    n = Notebook()
    n.add_note("Hello world")
    n.add_note("Hello again")
    assert n.total_notes() == 2


def test_remove_note():
    """
    Test the remove_note method
    """
    n = Notebook()
    n.add_note("Hello world")
    n.add_note("Hello again")
    n.remove_note(0)
    assert n.notes == ["Hello again"]


def test_remove_note_error():
    """
    Test the remove_note method with invalid input
    """
    n = Notebook()
    with pytest.raises(IndexError):
        n.remove_note(0)


def test_remove_note_error2():
    """
    Test the remove_note method with invalid input
    """
    n = Notebook()
    n.add_note("Hello world")
    with pytest.raises(IndexError):
        n.remove_note(3)


def test_clear():
    """
    Test the clear method
    """
    n = Notebook()
    n.add_note("Hello world")
    n.add_note("Hello again")
    n.clear()
    assert n.notes == []


def test_find():
    """
    Test the find method
    """
    n = Notebook()
    n.add_note("Hello world")
    n.add_note("Hello again")
    n.add_note("Goodbye")
    assert n.find("Hello") == ["Hello world", "Hello again"]


def test_find_empty():
    """
    Test the find method with no matching notes
    """
    n = Notebook()
    n.add_note("Goodbye")
    assert n.find("Hello") == []


def test_find_empty_notebook():
    """
    Test the find method with an empty notebook
    """
    n = Notebook()
    assert n.find("Hello") == []


def test_find_error():
    """
    Test the find method with invalid input
    """
    n = Notebook()
    with pytest.raises(TypeError):
        n.find(5)


def test_eq():
    """
    Test the eq method
    """
    n1 = Notebook()
    n1.add_note("Hello world")
    n1.add_note("Hello again")
    n2 = Notebook()
    n2.add_note("Hello world")
    n2.add_note("Hello again")
    assert n1 == n2


def test_eq_error():
    """
    Test the eq method with invalid input
    """
    n = Notebook()
    assert not (n == 5)


def test_str():
    """
    Test the str method
    """
    n = Notebook()
    n.add_note("Hello world")
    n.add_note("Hello again")
    assert str(n) == "Hello world\nHello again"


def test_notebook_save_to_file():
    """
    Test the save_to_file method
    """
    # create a notebook and add some notes
    n = Notebook()
    n.add_note("Hello")
    n.add_note("World")
    # this will create a temporary file and return its path
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
    n.save_to_file(file_path)
    with open(file_path, "r") as f:
        assert f.read() == "Hello\nWorld\n"
    os.remove(file_path)


def test_notebook_load_from_file():
    """
    Test the load_from_file method
    """
    # create a notebook and add some notes
    n = Notebook()
    # this will create a temporary file and return its path
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
    with open(file_path, "w") as f:
        f.write("Hello\nWorld\n")
    n.load_from_file(file_path)
    assert n.notes == ["Hello", "World"]
    os.remove(file_path)


def test_notebook_load_from_file_error():
    """
    Test the load_from_file method with invalid input
    """
    n = Notebook()
    with pytest.raises(FileNotFoundError):
        n.load_from_file("nonexistent.txt")
