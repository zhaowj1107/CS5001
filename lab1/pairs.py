'''
File: nest.py
Author: Chenjiesheng Yang / Weijian Zhao (David)
Date: 2025-01-07
Class: CS_5001, Spring_2025
Description:
Enter your description here 
'''


def main():
    a = int(input("Please fill in the first number: "))
    b = int(input("Please fill in the second number: "))
    c = int(input("Please fill in the third number: "))
    d = int(input("Please fill in the fourth number: "))

    if a == b:
        if c == d:
            print("two pairs")
        else:
            print("not two pairs")
    elif a == c:
        # a not equal b
        if b == d:
            print("two pairs")
        else:
            print("not two pairs")
    elif a == d:
        # a not equal b and c
        if b == c:
            print("two pairs")
        else:
            print("not two pairs")
    else:
        print("not two pairs")


if __name__ == "__main__":
    main()
