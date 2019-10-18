#!/usr/bin/python3
# Exercise 8-3 calc.py with regex
# Page 182-183
import re
import sys

def get_equation():
    try:
        op, nums = split_regex(input(
            "Enter equation in form [Val] [operator] [Val2]:"
            ))
        values_list = []
        try:
            for i in nums:
                values_list.append(int(i))
        except ValueError:
            pass
        finally:
            if len(values_list) < 2:
                raise IndexError
            else:
                return op, values_list
    except IndexError:
        print(
            "Equation not in form [Val] [operator] [Val2]:"
            )
        sys.exit(1)

def split_regex(stringy):
    numbers = r"[+\-\*/]"
    operator = r""
    return (re.search(numbers, stringy).group()[0],
            re.split(numbers, stringy))

def addition(numbers):
    result = 0
    for i in numbers:
        result += i
    return result

def subtraction(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result -= i
    return result

def division(numbers):
    result = numbers[0]
    try:
        for i in numbers[1:]:
            result /= i
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        sys.exit(1)
    return result

def custom_math(operator, numbers):
    math_dict = {
                 "+": addition,
                 "-": subtraction,
                 "/": division
                 }

    return(math_dict[operator](numbers))

if __name__ == "__main__":
    matched_operator = None

    while not matched_operator:
        matched_operator, number_list = get_equation()
        print(custom_math(matched_operator, number_list))


