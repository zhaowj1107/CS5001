import unittest
from class_pizza import Pizza

class UnittestPizza(unittest.TestCase):
    def test_get_3toppings(self):
        my_fav = Pizza('tomato',"mushroom","onion")
        self.assertEqual(my_fav.get_toppings(), ['tomato','mushroom','onion'])
    
    def test_get_2toppings(self):
        my_fav = Pizza(None,"mushroom","onion")
        self.assertEqual(my_fav.get_toppings(), ['mushroom','onion'])
    
    def test_calculate_price(self):
        my_fav = Pizza("mushroom","onion")
        self.assertEqual(my_fav.calculate_price(), 13)
    
    def test_get_topings(self):
        my_fav = Pizza(None,"mushroom","onion")
        self.assertEqual(str(my_fav), "Pizza with toppings: ['mushroom', 'onion']")

if __name__ == "__main__": # pragma: no cover
    unittest.main() 