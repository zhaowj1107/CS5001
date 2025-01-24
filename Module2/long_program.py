''' Restaurant Management System
    CS5001
    Sample code -- a long program with only main function.
'''

from restaurant_management_tools import display_menu, compute_price, calculate_final_bill

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

# Run the main function
main()
