''' Restaurant Management System
    CS5001
    Sample code -- a long program with only main function.
'''
def do_order(order):
    ''' Function order_food
        Parameters: string
        Returns: price
    '''
    if order == "Burger":
        price = 5.00
    elif order == "Pizza":
        price = 8.00
    elif order == "Salad":
        price = 4.50
    else:
        print("Invalid item, charging $0.00.")
        price = 0.00
    return price
    

def main():
    ''' Function main
        Parameters: none
        Returns: nothing
    '''
    # Display Menu
    print("Menu:\n"
          "1. Burger - $5.00\n"
          "2. Pizza - $8.00\n"
          "3. Salad - $4.50\n")

    # Process Order
    order1 = input("What would you like to order?\n")
    do_order(order1)
    total_price = do_order(order1)

    print("...\n")

    order2 = input("Would you like to order anything else?\n")
    do_order(order2)
    total_price = do_order(order2)
    

    print("...\n")

    # Calculate Final Bill
    discount = float(input("Enter discount percentage (if any):\n"))
    total_bill = total_price - (total_price * discount / 100)
    print("Your total bill is $", total_bill, sep="")

# Run the main function
main()

"""
Feedback_Weijian.zhao
1. maybe you should define the variabe "total_price", but it is not necessary.
2. you should define the variable "price" in the global scope, so that you can use it in the do_order function, but it is not necessary too.
3. Lino def display_menu and calculate_discount function, but it is not necessary too from my perspective.  
"""
    
