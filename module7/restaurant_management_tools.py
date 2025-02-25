def read_menu(file_name="menu.csv"):
    menu = {}
    file_path = "Project/CS5001/module7/"
    try:
        with open(file_path + file_name, "r") as file:
            for line in file:
                # check if there is invalid data structure
                try:
                    item, price = line.strip().split(",")
                    menu[item] = float(price)
                except ValueError:
                    print(f"Warning: Invalid format in line: {line.strip()}")
                    continue
        return menu
    # check the file is valid
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found in directory 'Project/CS5001/module7/'")
        return {}
    except PermissionError:
        print("Error: Insufficient permissions to read the file!")
    # something I have no idea
    except IOError as e:
        print(f"Error reading file: {e}")
        return {}

def display_menu(menu):
    '''
        Function display_menu()
        Parameters: menu (dict) - dictionary containing menu items and prices
        Returns: none
        Handles: 
            - Empty menu case
            - Invalid menu data types
    '''
    if not menu:
        print("Warning: The menu is empty!")
        return
        
    if not isinstance(menu, dict):
        print("Error: Invalid menu format. Expected a dictionary.")
        return
        
    try:
        print("Menu:")
        number = 1
        for item, price in menu.items():
            if not isinstance(item, str) or not isinstance(price, (int, float)):
                print(f"Warning: Invalid data type for item {item} or its price")
                continue
            print(f"{number}. {item}: ${price:.2f}")
            number += 1
    except Exception as e:
        print(f"Error displaying menu: {e}")


def compute_price(price, order, menu):
    '''
        Function compute_price()
        Parameters: price (float), order (string)
        Returns: price (float)
    '''
    if order in menu:
        price += menu[order]
    else:
        print("Invalid item, charging $0.00.")
        price += 0.00

    print("...\n")
    return price

def calculate_final_bill(price, discount):
    '''
        Function calculate_final_bill()
        Parameters: price (float), discount (float)
        Return: bill (float)
        Example:
        >>> calculate_final_bill(10.00, 10)
        9.0
        >>> calculate_final_bill(20.00, 25)
        15.0
        >>> calculate_final_bill(30.00, 100)
        0.0
    '''
    bill = price - (price * discount / 100)
    return bill

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
