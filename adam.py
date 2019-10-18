
length_1 = 25
length_2 = 15

height_1 = 30
height_2 = 40


column = "height"
variables = globals()

items = [
    pair
    for pair in variables.items()
    if pair[0].startswith(column)
]


print(items)
# total = 0
# for k in keys:
#     total += variables[k]

# print("Total ", column, total)
