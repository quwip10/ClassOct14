#!/usr/bin/env python


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x/y


functions = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,
    "**": pow,
    "^": pow
}


while True:
    expr = input("Enter a math expression: ")

    if expr.lower() == 'q':
        break

    v1, op, v2 = expr.split()
    v1 = float(v1)
    v2 = float(v2)

    if op in functions:
        result = functions[op](v1, v2)
        print("{:.3f}".format(result))
    else:
        print("no op")
