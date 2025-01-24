''' Restaurant Management System
    CS5001
    Sample code -- a long program with only main function.
'''

def display_menu():
    '''
        Function display_menu()
        Parameters: none
        Returns: none
    '''
    print("Menu:\n"
          "1. Burger - $5.00\n"
          "2. Pizza - $8.00\n"
          "3. Salad - $4.50\n")

def compute_price(price, order):
    '''
        Function compute_price()
        Parameters: price (float), order (string)
        Returns: price (float)
    >>> compute_price(0, "Burger")
    5.0
    >>> compute_price(12, "Pizza")
    20.0
    >>> compute_price(100000, "Salad")
    100004.5
    >>> compute_price(1000000, "Sandiwch")
    Invalid item, charging $0.00.
    1000000.0
    '''
    if order == "Burger":
        price += 5.00
    elif order == "Pizza":
        price += 8.00
    elif order == "Salad":
        price += 4.50
    else:
        print("Invalid item, charging $0.00.")
        price += 0.00

    #print("...\n")
    return price

def calculate_final_bill(price, discount):
    '''
        Function calculate_final_bill()
        Parameters: price (float), discount (float)
        Return: bill (float)
    >>> calculate_final_bill(5.00, 10)
    4.5
    >>> calculate_final_bill(20.00, 25)
    15.0
    >>> calculate_final_bill(4.50, 100)
    0.0
    '''
    bill = price - (price * discount / 100)
    return bill
"""
def main():
    ''' Function main
        Parameters: none
        Returns: nothing
    '''
    # Display Menu
    display_menu()

    # Initialize price
    current_price = 0.00
    
    # Order first item
    user_order = input("What would you like to order?\n")
    current_price = compute_price(current_price, user_order)

    # Order second item
    user_order = input("Would you like to order anything else?\n")
    current_price = compute_price(current_price, user_order)

    # Calculate Final Bill
    user_discount = float(input("Enter discount percentage (if any):\n"))
    total_bill =calculate_final_bill(current_price, user_discount)
    print("Your total bill is $", total_bill, sep="")
"""
# Run the main function
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)