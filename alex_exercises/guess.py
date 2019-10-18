#!/usr/bin/env

user_num = -1
min_val = 0
max_val = 1000
guess = -2

while not min_val <= user_num <= max_val:
    user_num = int(input("Enter a number between {} and {}: ".format(min_val, max_val)))

guess = (min_val + max_val) // 2

while guess != user_num:

    print("My guess is {}".format(guess))
    low_high = input("Enter 'L' for too low or 'H' for too high: ")

    while low_high.upper() not in ('L', 'H'):
        low_high = input("Enter 'L' for too low or 'H' for too high: ")

    if low_high.upper() == 'L':
        min_val = guess
    else:
        max_val = guess

    guess = (min_val + max_val) // 2

print("I figured it out! Your number is: {}".format(guess))
