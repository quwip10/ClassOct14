

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


assorted_pies = sorted(pies, key=pie_ranking)

for pie in assorted_pies:
    print(pie)
