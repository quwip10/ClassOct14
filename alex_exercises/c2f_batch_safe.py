#!/usr/bin/python3
# Exercise 10-1
# Page 219
# Rewrite with error handling for non-numbers
import sys

def c2f(c_num):
    return (c_num * (9/5) +32)
for i in sys.argv[1:]:
    try:
        print("Temp in F: ", c2f(float(i)))
    except ValueError:
        print("{} is not a valid temperature."
            "Please enter only digits".format(
            i))
