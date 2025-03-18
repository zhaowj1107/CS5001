import pytest
from class_pizza import Pizza

def test_get_3toppings():
    my_fav = Pizza('tomato',"mushroom","onion")
    assert my_fav.get_toppings() == ['tomato','mushroom','onion']


def test_get_2toppings():
    my_fav = Pizza(None,"mushroom","onion")
    assert my_fav.get_toppings() == ['mushroom','onion']


def test_calculate_price():
    my_fav = Pizza("mushroom","onion")
    assert my_fav.calculate_price() == 13


def tet_get_topings():
    my_fav = Pizza(None,"mushroom","onion")
    assert str(my_fav) == "Pizza with toppings: ['mushroom', 'onion']"


if __name__ == "__main__":
    pass