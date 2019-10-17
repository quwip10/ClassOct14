

def insensivitive_sort(pie):
    return pie.lower()


def pie_ranking(pie):
    top_pies = ["apple", "pumpkin"]
    lowercased = pie.lower()
    if lowercased in top_pies:
        return (0, lowercased)
    else:
        return (1, lowercased)


pies = ["key lime", "apple", "Pumpkin",
        "cherry", "french silk", "Blueberry",
        "huckleberry", "strawberry rhubarb", "Cheese cake"]

assorted_pies = sorted(pies, key=str.lower)

for pie in assorted_pies:
    print(pie)

print("-" * 20)


# def pie_with_ranks(pie):
#     return -pie[1], pie[0].lower()


ranked_pies = [
    ("key lime", 4),
    ("apple", 5),
    ("Pumpkin", 5),
    ("cherry", 3),
    ("french silk", 3),
    ("Blueberry", 4),
    ("huckleberry", 4),
    ("strawberry rhubarb", 3),
    ("Cheese cake", 2)
]

# def sort_by_lastName(row):
#     return row.last_name


# s = sorted(df, key= lambda row: row.last_name)


ranked = sorted(ranked_pies, key=lambda pie: (-pie[1], pie[0].lower()))


for p in ranked:
    print(p)


def cool_func(f):
    f(1, 2)


cool_func(lambda a, b: a + b)
