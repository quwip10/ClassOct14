#!/usr/bin/python3
import sys

def my_func(filename):
   with open(filename, "r") as txt_file:
       for line_num, line in enumerate(txt_file):
           print(str("{:2}").format(line_num), line.strip())

if len(sys.argv) > 1:
    for path in sys.argv[1:]:
         my_func(path)
else:
    my_func("../DATA/tyger.txt")
