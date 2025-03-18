''' pizza_class.py
    This module contains the class definition for a pizza.
    CS5001
    2025/03/10
'''

class Pizza:
    ''' Class Pizza
        Attributes: toppings (list)
    '''
    def __init__(self,topping1 = None,topping2 = None,topping3 = None):
        ''' Constructor for Pizza
            Parameters: topping1, topping2, topping3 (str)
            Returns: nothing
        '''
        self.toppings = [topping1,topping2,topping3]

    def get_toppings(self):
        ''' Method get_toppings
            Parameters: none
            Returns: list
        '''
        self.toppings = [topping for topping in self.toppings if topping is not None]
        return self.toppings
    
    def calculate_price(self):
        price = 10
        for i in range(len(self.toppings)):
            price += 1
        return price
    
    def __str__(self):
        self.toppings = [topping for topping in self.toppings if topping is not None]
        return "Pizza with toppings: " + str(self.toppings)


if __name__ == "__main__":
    my_fav = Pizza(None,"mushroom","onion")
    print(my_fav.get_toppings())
    print(my_fav.calculate_price())