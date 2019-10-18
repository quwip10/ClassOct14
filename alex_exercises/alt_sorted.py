#!/usr/bin/python3
# Exercise 9-2
# Page 204

a_words = []
b_words = []

with open("../DATA/alt.txt") as data_file:
   for line in data_file:
        if line[0].lower() == 'a':
            a_words.append(line.strip())
        else:
            b_words.append(line.strip())

with open("./a_sorted.txt", "w") as a_file:
    for line in sorted(a_words):
        a_file.writelines(line + "\n")

with open("./b_sorted.txt", "w") as b_file:
    for line in sorted(b_words, reverse=True):
        b_file.writelines(line + "\n")
