
names = ["adam", "alex", "jared", "jed", "jennifer"]
names.append("kevin")
names.append("mark")
names.append("rob")
names.append("jared")
names.extend(["thomas", "trang", "susan"])


person = names.pop()
person = names.pop(6)

jared_count = names.count("jared")

names[8] = "tom"

names.remove("adam")  # rage quit

# current status of names
print(names)


number_of_names = len(names)  # 5 names

first_person = names[0]

characters = len(first_person)  # 4 characters


# PEP 8
# Pythonic
long_string = ("this is a long string. "
               "It goes on for many characters. "
               "Way beyond the 79 character limit. But too bad . "
               " It is my class and I do what it want")


# the following is not a list, but a tuple

#              name           age  hometown
instructor = ("rob foulkrod", 47, "detroit")


name = instructor[0]
age = instructor[1]
home_town = instructor[2]

name, age, home_town = instructor  # unpacking, it is the same as above

line = "rob,red,dogs,detroit"
name, _, _, home_town = line.split(",")  # underscore is a throw-away variable


names = ["adam", "alex", "Jared", "JED", "jennifer  "]
names.append("kevin")
names.append("  mark  ")
names.append("roB")
names.extend(["thomas", "trAng", "susan"])


# clean_names = []
# for n in names:
#     cleaned_name = n.strip().lower()
#     clean_names.append(cleaned_name)

cleaned_names = [
    n.lower().strip()          # 3 select  -> transform
    for n in names             # 1 from  -> Data Source
    if len(n.strip()) > 4      # 2 where -> Filter
]


censored_names = [
    "####" if len(n) == 4 else "---" if len(n) == 3 else n
    for n in names
    # not needed
]


print("names", names)
print("cleaned_names", cleaned_names)
print("censored_names", censored_names)


name_check = input("who are you looking for? ")

is_in_list = name_check in cleaned_names

msg = "yes" if is_in_list else "no"
