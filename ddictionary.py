import collections


def simple_default():
    return "flat"


states = collections.defaultdict(simple_default,
                                 {"FL": "awesome", "MD": "Great", "CO": "Rocky"})

result = states["OH"]
print(result)


next_id = 0


def auto_number():
    global next_id
    next_id = next_id + 1
    return next_id


def auto_number_generator(initial_number=1):
    id = initial_number - 1

    def next():
        nonlocal id
        id += 1
        return id
    return next


pies = collections.defaultdict(auto_number_generator())
apple = pies["apple"]  # 1
cherry = pies["cherry"]  # 2
pumpkin = pies["pumpkin"]  # 3
print(pies)

cookies = collections.defaultdict(auto_number_generator(initial_number=101))
chip = cookies["chocolatechip"]
sugar = cookies["sugar"]
print(cookies)

# import copy


# names = ["Trang", "Thomas", "Susan", "Rob", "Mark"]

# selected_people = names[:]

# selected_people.append("adam")

# list_of_list = [names, selected_people]

# deep_copy = copy.deepcopy(list_of_list)

# deep_copy[0].append("Kevin")
# deep_copy[0].append("Jennifer")


# print(deep_copy[0])
# print(list_of_list[0])
