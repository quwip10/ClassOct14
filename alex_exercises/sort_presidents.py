#!/usr/bin/python3
# Exercise 9-4
# Page 204

presidents_list = []
with open("../DATA/presidents.txt") as presidents_file:
    for line in presidents_file:
        presidents_list.append(line.split(":"))

for president in sorted(presidents_list,
                        key=lambda e: (e[1],e[2])
                       ):
                        for i in president:
                            print(i, sep=" ")
                        print()

