
from pprint import pprint as pp
incomes = {"mi": 50000, "fl": 55000, "oh": 57000}

income1 = incomes["mi"]
print("mi", income1)

# if "nj" in incomes:
#     income1 = incomes["nj"]
#     print("nj", income1)
# else:
#     print("no jersey")

income2 = incomes.get("nj", "--")

print("nj", income2)

print("All Keys")
for k in incomes.keys():
    print(k)

print()

print("All values")
for v in incomes.values():
    print(v)

print()

print("All pairs")
for p in incomes.items():
    print(p)


if 50000 in incomes.values():
    print("someone makes that")
else:
    print("nope")

# make the data more difficult


incomes["ca"] = [70000, 65000, 40000, 80000]
incomes["wa"] = {"ab": 50000, "cd": 60000}


print()
print("What the dictionalry looks like printed")
print(incomes)

print("the pretty version")
pp(incomes)
