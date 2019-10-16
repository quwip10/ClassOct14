
good_breakfast = {"coffee", "bacon", "protein smoothie",
                  "coffee", "bacon", "breakfast pizza", "eggs", "waffles", "green eggs"}

print("breakfast foods", len(good_breakfast))
print(good_breakfast)

breakfast_on_hand = {"coffee", "cereal",
                     "stale donuts", "oatmeal", "green eggs"}

common = good_breakfast.intersection(breakfast_on_hand)
common = good_breakfast & breakfast_on_hand


print("happy", common)

all = breakfast_on_hand.union(good_breakfast)
all = breakfast_on_hand | good_breakfast

print("all", all)

unhappy = good_breakfast - breakfast_on_hand
print("unhappy", unhappy)
