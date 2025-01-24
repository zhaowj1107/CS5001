'''
File: build_string.py
Author:  / Weijian Zhao (David)
Date: 2025-01-22
Class: CS_5001, Spring_2025

'''

def build_string(string, num1, num2, num3):
    string = str(string)
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    string1 = string*num1+"\n"
    string2 = string*num2+"\n"
    string3 = string*num3
    string_total = string1 + string2 + string3
    return string_total

if __name__ == "__main__":
    build_string("hi",0,3,4)