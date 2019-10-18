#!/usr/bin/python3
# Exercise 14-2
# Page 313
import os.path, sys

for i in sys.argv[1:]:
    if os.path.isfile(i):
        print("{} Size: {}".format(i, os.path.getsize(i)))
    else:
        print("{} is not a valid file.".format(i))
