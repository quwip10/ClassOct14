#!/usr/bin/python3
# Exercise 12-1 Part2
# Page 256
import sys
from knight import Knight

if __name__ == '__main__':

    some_knights = []

    for i in sys.argv[1:]:
        try:
            some_knights.append(Knight(i))
        except ValueError:
            print("{} not found in knights.txt".format(i))

    for knight in some_knights:
        print("Name: {} {}\n"
               "Favorite Color: {}\n"
               "Quest: {}\n"
               "Comment: {}"
               .format(
                        knight.title, knight.name,
                        knight.favorite_color,
                        knight.quest,
                        knight.comment
                ))
