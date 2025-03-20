import unittest
from name import Name

class TestName(unittest.TestCase):
    def test_constructor(self):
        name = Name("John", "Doe")
        self.assertEqual(name.get_first_name(), "John")
        self.assertEqual(name.get_last_name(), "Doe")
        self.assertEqual(name.get_full_name(), "John Doe")
        self.assertEqual(name.get_nick_name(), "John")

    def test_constructor_invalid_first_name(self):
        with self.assertRaises(TypeError):
            Name(123, "Doe")
    
    def test_constructor_invalid_last_name(self):
        with self.assertRaises(TypeError):
            Name("John", 123)
    
    def test_constructor_empty_first_name(self):
        with self.assertRaises(ValueError):
            Name("", "Doe")

    def test_constructor_empty_last_name(self):
        with self.assertRaises(ValueError):
            Name("John", "")
        
    def test_set_nick_name_empty(self):
        name = Name("John", "Doe")
        with self.assertRaises(ValueError):
            name.set_nick_name("")
    
    def test_set_nick_name_invalid(self):
        name = Name("John", "Doe")
        with self.assertRaises(TypeError):
            name.set_nick_name(123)
    
    def test_str(self):
        name = Name("John", "Doe")
        self.assertEqual(str(name), 'John "John" Doe')
    
    def test_set_nick_name(self):
        name = Name("John", "Doe")
        name.set_nick_name("Johnny")
        self.assertEqual(name.get_nick_name(), "Johnny")
        
    def test_equal(self):
        name1 = Name("John", "Doe")
        name2 = Name("John", "Doe")
        self.assertEqual(name1, name2)
    
    def test_inequal(self):
        name1 = Name("John", "Doe")
        name2 = Name("Jane", "Doe")
        self.assertNotEqual(name1, name2)
    

    def test_first_name_with_number(self):
        with self.assertRaises(ValueError):
            Name("dav123", "Doe")
    
    def test_last_name_with_number(self):
        with self.assertRaises(ValueError):
            Name("John", "john123")
    
    def test_nick_name_with_number(self):
        name = Name("John", "Doe")
        with self.assertRaises(ValueError):
            name.set_nick_name("john123")
    
    def test_last_name_with_speicial_character(self):
        with self.assertRaises(ValueError):
            Name("John", "Doe@")

    def test_nick_name_with_number(self):
        name = Name("John", "Doe")
        with self.assertRaises(ValueError):
            name.set_nick_name("john@")
    
    def test_first_name_with_special_character(self):
        with self.assertRaises(ValueError):
            Name("John@", "Doe")

    def test_last_name_with_space(self):
        with self.assertRaises(ValueError):
            Name("John", "Do e@")
    
    def test_nick_name_with_number(self):
        name = Name("John", "Doe")
        with self.assertRaises(ValueError):
            name.set_nick_name("john 123")
    
    def test_first_name_with_space(self):
        with self.assertRaises(ValueError):
            Name("John@", "Do e")

    def test_equal_invalid(self):
        name = Name("John", "Doe")
        with self.assertRaises(TypeError):
            self.assertEqual(name, 123)

if __name__ == "__main__": # pragma: no cover
    unittest.main()