import os
print(os.getcwd())

menu = {}
with open("Project/CS5001/module7/menu.csv", "r") as file:
    for line in file:
        item, price = line.strip().split(",")
        menu[item] = float(price)
print(menu)