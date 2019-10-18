#!/usr/bin/python3
# Exercise 13-1
# Page 282
import re, sys

for fil in sys.argv[2:]:
    search_term = sys.argv[1]

    with open(fil) as text:
        for line in text:
            if re.search(search_term, line):
                print(line)
