from timeit import default_timer as timer

def print_numbers_version_one():
    number = 2
    list = []
    while number <= 2**15:
        # If number is even, print it:
        if number % 2 == 0:
            list.append(number)
        #print(number)
        number += 1

def print_numbers_version_one():
    number = 2
    list = []
    while number <= 2**15:
        # If number is even, print it:
        #print(number)
        list.append(number)
        number += 2

start = timer()
print_numbers_version_one()
end = timer()
print("The runtime of recursive fibonacci without memoization :", round(end - start,6), "seconds")


start = timer()
print_numbers_version_one()
end = timer()
print("The runtime of recursive fibonacci with memoization :", round(end - start,6), "seconds")