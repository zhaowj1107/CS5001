''' Restaurant Management System
    CS5001
    Sample code -- a long program with only main function.

'''
def display_menu():
    ''' Function display_menu
        Parameters: none
        Returns: nothing
    '''
    print("Menu:\n"
          "1. Burger - $5.00\n"
          "2. Pizza - $8.00\n"
          "3. Salad - $4.50\n")

def order_book(order, accum_price = 0):
    ''' Function order_book
        Parameters: order,accum_price
        Returns: accum_price
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
    accum_price = price + accum_price
    print(f"The price of your order is ${price}, The current bill is ${accum_price}")
    return accum_price

def final_bill(accum_price, discount = 0):
    ''' Function final_bill
        Parameters: accum_price,discount
        Returns: nothing
    '''
    total_bill = accum_price - (accum_price * discount / 100)
    print("Your total bill is $", total_bill, sep="")    

def main():
    ''' Function main
        Parameters: none
        Returns: nothing
    '''
    # Display Menu
    display_menu()
    accum_price = 0

    # Process Order
    order = input("What would you like to order?\n")
    accum_price = order_book(order, accum_price)

    print("...\n")

    order = input("Would you like to order anything else?\n")
    accum_price = order_book(order, accum_price)

    print("...\n")

    # Calculate Final Bill
    discount = float(input("Enter discount percentage (if any):\n"))
    final_bill(accum_price, discount)

# Run the main function
main()
    
