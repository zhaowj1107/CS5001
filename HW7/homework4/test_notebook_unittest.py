"""
File: test_notebook_unittest.py
Author: Weijian Zhao(David)
Date: 2025-03-18
Class: CS_5001, Spring_2025
Description: 
homework 7: test_Shapes
"""
import os
import unittest
import tempfile
from notebook import Notebook


class TestNotebook(unittest.TestCase):
    def test_constructor(self):
        """
        Test the constructor
        """
        n = Notebook()
        self.assertEqual(n.notes, [])
    
    def test_add_note(self):
        """
        Test the add_note method
        """
        n = Notebook()
        n.add_note("Hello world")
        self.assertEqual(n.notes, ["Hello world"])
    
    def test_add_note_error(self):
        """
        Test the add_note method with invalid input
        """
        n = Notebook()
        with self.assertRaises(TypeError):
            n.add_note(5)

    def test_get_note(self):
        """
        Test the get_note method
        """
        n = Notebook()
        n.add_note("Hello world")
        self.assertEqual(n.get_note(0), "Hello world")
    
    def test_get_note_error(self):
        """
        Test the get_note method with invalid input
        """
        n = Notebook()
        with self.assertRaises(IndexError):
            n.get_note(0)
    
    def test_get_note_error2(self):
        """
        Test the get_note method with invalid input
        """
        n = Notebook()
        n.add_note("Hello world")
        with self.assertRaises(IndexError):
            n.get_note(3)
    
    def test_total_notes(self):
        """
        Test the total_notes method
        """
        n = Notebook()
        n.add_note("Hello world")
        n.add_note("Hello again")
        self.assertEqual(n.total_notes(), 2)
    
    def test_remove_note(self):
        """
        Test the remove_note method
        """
        n = Notebook()
        n.add_note("Hello world")
        n.add_note("Hello again")
        n.remove_note(0)
        self.assertEqual(n.notes, ["Hello again"])
    
    def test_remove_note_error(self):
        """
        Test the remove_note method with invalid input
        """
        n = Notebook()
        with self.assertRaises(IndexError):
            n.remove_note(0)
    
    def test_remove_note_error2(self):
        """
        Test the remove_note method with invalid input
        """
        n = Notebook()
        n.add_note("Hello world")
        with self.assertRaises(IndexError):
            n.remove_note(3)

    def test_clear(self):
        """
        Test the clear method
        """
        n = Notebook()
        n.add_note("Hello world")
        n.add_note("Hello again")
        n.clear()
        self.assertEqual(n.notes, [])
    
    def test_find(self):
        """
        Test the find method
        """
        n = Notebook()
        n.add_note("Hello world")
        n.add_note("Hello again")
        n.add_note("Goodbye")
        self.assertEqual(n.find("Hello"), ["Hello world", "Hello again"])

    def test_find_empty(self):
        """
        Test the find method with no matching notes
        """
        n = Notebook()
        n.add_note("Goodbye")
        self.assertEqual(n.find("Hello"), [])

    def test_find_empty_notebook(self):
        """
        Test the find method with an empty notebook
        """
        n = Notebook()
        self.assertEqual(n.find("Hello"), [])
    
    def test_find_error(self):
        """
        Test the find method with invalid input
        """
        n = Notebook()
        with self.assertRaises(TypeError):
            n.find(5)
    
    def test_eq(self):
        """
        Test the eq method
        """
        n1 = Notebook()
        n1.add_note("Hello world")
        n1.add_note("Hello again")
        n2 = Notebook()
        n2.add_note("Hello world")
        n2.add_note("Hello again")
        self.assertEqual(n1, n2)
    
    def test_eq_error(self):
        """
        Test the eq method with invalid input
        """
        n = Notebook()
        self.assertFalse(n == 5)
    
    def test_str(self):
        """
        Test the str method
        """
        n = Notebook()
        n.add_note("Hello world")
        n.add_note("Hello again")
        self.assertEqual(str(n), "Hello world\nHello again")
    
    def test_notebook_save_to_file(self):
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
            self.assertEqual(f.read(), "Hello\nWorld\n")
        os.remove(file_path)

    def test_notebook_load_from_file(self):
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
        self.assertEqual(n.notes, ["Hello", "World"])
        os.remove(file_path)
    
    def test_notebook_load_from_file_error(self):
        """
        Test the load_from_file method with invalid input
        """
        n = Notebook()
        with self.assertRaises(FileNotFoundError):
            n.load_from_file("nonexistent.txt")


if __name__ == "__main__": # pragma: no cover
    unittest.main()
