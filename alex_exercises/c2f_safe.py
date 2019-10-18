#!/usr/bin/python3
# Exercise 10-1
# Page 219
# Rewrite with error handling for non-numbers

def c2f(c_num):
    return (c_num * (9/5) +32)
while True:
    try:
        temp = input("Enter temp in C: ")
        if temp in ['q', 'Q', 'quit', 'Quit', 'exit']:
            break

        print("Temp in F: ", c2f(float(temp)))
    except ValueError:
        print("Please enter only digits")
