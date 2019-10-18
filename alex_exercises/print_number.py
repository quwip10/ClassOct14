#!/usr/bin/python3
# Exercise 13-3
# Page 282
import re

search_term = re.compile(r'\b\d{0,3}-?\d{3}-?\d{4}\b')

with open("../DATA/custinfo.dat") as input_txt:
    for line in input_txt:
        if search_term.findall(line):
            print(line.strip())
