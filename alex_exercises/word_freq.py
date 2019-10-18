#!/usr/bin/python3
# Exercise 13-4
# Page 282
import re, sys

delimit_split = re.compile(r"[^\w']+")
count_dict = dict()

with open(sys.argv[1]) as in_txt:
    for line in in_txt:
        for word in delimit_split.split(line):
           count_dict[word.lower()] =\
           count_dict.get(word.lower(), 0) + 1

for word, count in sorted(count_dict.items(),
                          key = lambda e: (-e[1], e[0])
                          ):
    print(word, count)
