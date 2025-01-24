''' Restaurant Management System
    CS5001
    Sample code -- a long program with only main function.

'''

def order_book():
    order = input("What would you like to order?\n")
    if order == "Burger":
        price = 5.00
    elif order == "Pizza":
        price = 8.00
    elif order == "Salad":
        price = 4.50
    else:
        print("Invalid item, charging $0.00.")
        price = 0.00

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
    order = input("What would you like to order?\n")
    if order == "Burger":
        price = 5.00
    elif order == "Pizza":
        price = 8.00
    elif order == "Salad":
        price = 4.50
    else:
        print("Invalid item, charging $0.00.")
        price = 0.00

    print("...\n")

    order = input("Would you like to order anything else?\n")
    if order == "Burger":
        price += 5.00
    elif order == "Pizza":
        price += 8.00
    elif order == "Salad":
        price += 4.50
    else:
        print("Invalid item, charging $0.00.")
        price += 0.00

    print("...\n")

    # Calculate Final Bill
    discount = float(input("Enter discount percentage (if any):\n"))
    total_bill = price - (price * discount / 100)
    print("Your total bill is $", total_bill, sep="")

# Run the main function
main()
    