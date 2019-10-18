#!/usr/bin/python3
import sys


def output_a_b(filename):
    with open(filename, "r") as txt_file:
        with open("a.txt", "w") as a_file:
            with open("b.txt", "w") as b_file:
                for line in txt_file:
                    if line[0] == 'a':
                        a_file.writelines(line)
                    else:
                        b_file.writelines(line)


if len(sys.argv) > 1:
    for path in sys.argv[1:]:
        output_a_b(path)
else:
    output_a_b("../DATA/alt.txt")
