import random


suits = ["C", "D", "H", "S"]
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

deck = [
    (r, s)
    for r in ranks
    for s in suits
]

print(deck)
print()

random.shuffle(deck)
print(deck)


print(deck.pop())
print(deck.pop())
