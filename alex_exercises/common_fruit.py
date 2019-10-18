#!/usr/local/bin/python3

fruit1_set = set()
fruit2_set = set()

with open("../DATA/fruit1.txt", "r") as fruit1,\
     open("../DATA/fruit2.txt", "r") as fruit2:
    for line in fruit1:
        fruit1_set.add(line.strip().lower())
    for line in fruit2:
        fruit2_set.add(line.strip().lower())

intersection_set = fruit1_set & fruit2_set

for i in intersection_set: print(i)
