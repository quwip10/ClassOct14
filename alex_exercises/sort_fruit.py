#!/usr/bin/python3
# Exercise 9-3
# Page 204

fruit_list = []

with open("../DATA/fruit.txt") as fruit_file:
    for line in fruit_file:
        fruit_list.append(line.strip())

print("Sorted by name (case-sensitive):")
for fruit in sorted(fruit_list):
    print(fruit)
print()

print("Sorted by name (case-insensitive):")
for fruit in sorted(fruit_list, key=str.lower):
    print(fruit)
print()

print("Sorted by length of name, then by name:")
for fruit in sorted(fruit_list, key=lambda e: (len(e), e.lower())):
    print(fruit)
print()

print("Sorted by the 2nd letter of the name,"
      "then first letter:"
     )
for fruit in sorted(fruit_list,
                    key=lambda e: (e.lower()[1], e.lower()[0])
                   ):
    print(fruit)
print()
