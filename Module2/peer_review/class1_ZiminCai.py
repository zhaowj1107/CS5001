''' Restaurant Management System
    CS5001
    Sample code -- a long program with only main function.
'''



def menu():
    
    ''' Function order_1
        Parameters: none
        Returns: nothing
    '''
    print("Menu:\n"
          "1. Burger - $5.00\n"
          "2. Pizza - $8.00\n"
          "3. Salad - $4.50\n")


def order_1():
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

def order_2():
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

def main():
    menu()
    order_1()
    order_2()
    discount = float(input("Enter discount percentage (if any):\n"))
    total_bill = price - (price * discount / 100)
    print("Your total bill is $", total_bill, sep="")

main()

"""
Feedback_Weijian.zhao
1. you should define the variable "price" in the global scope, so that you can use it in the order_2 function.
2. your should conbime the order_1 and order_2 function into one function, and call it twice in the main function.
3. for the order function, you should return the price, so that you can use it in the main function.
4. write some comments for the functions.
5. the order function should have iput parameters, so that you can use it in the main function.

"""