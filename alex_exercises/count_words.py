#!/usr/bin/python3 import sys
import sys

def search_file(filename, keyword):
    search_count = 0
    with open(filename, "r") as alice_file:
        for line in alice_file:
            if keyword.lower() in line.lower().strip():
                search_count += 1
        return search_count

if len(sys.argv) > 1:
    search_term = sys.argv[1]
    for i in sys.argv[2:]:
        print(search_file(i, search_term))
else:
    print(search_file("../DATA/alice.txt", "Alice"))
