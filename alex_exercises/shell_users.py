#!/usr/bin/python3
shell_dict = {}

with open("../DATA/passwd", "r") as passwd:
    for line in passwd:
        key = line.rstrip().split(":")[-1]
        if key and key in shell_dict:
            shell_dict[key] += 1
        elif key:
            shell_dict[key] = 1

for i, j in shell_dict.items():
    print(i, j)

