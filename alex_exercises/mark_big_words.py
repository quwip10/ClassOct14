#!/usr/bin/python3
# Exercise 13-2
# Page 282
import re

search_term = re.compile(r'\b\w{8,}\b')

with open("../DATA/parrot.txt") as parrot_text:
    with open("./bigwords.txt", "w") as output_text:
        for line in parrot_text:
            for m in search_term.finditer(line):
                output_text.writelines(m.group() + "\n")
