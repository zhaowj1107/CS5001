''' Restaurant Management System
    CS5001
    Ordering food from a restaurant.
'''

import restaurant_management_tools as rmt

def main():
    ''' Function main
        Parameters: none
        Returns: nothing
    '''
    menu = rmt.read_menu()
    # Display Menu
    rmt.display_menu(menu)

    # Initialize price
    current_price = 0.00

    # Order first item
    user_order = input("What would you like to order?\n")
    current_price = rmt.compute_price(current_price, user_order, menu)

    # Order second item
    user_order = input("Would you like to order anything else?\n")
    current_price = rmt.compute_price(current_price, user_order, menu)

    # Calculate Final Bill
    user_discount = float(input("Enter discount percentage (if any):\n"))
    total_bill = rmt.calculate_final_bill(current_price, user_discount)
    print("Your total bill is $", total_bill, sep="")

# Run the main function
main()
