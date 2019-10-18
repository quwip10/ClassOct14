#!/usr/bin/python3

def grade(score):
    letter_grade = None

    if 95 <= score <= 100:
        letter_grade = 'A'
    elif 89 <= score <= 94:
        letter_grade = 'B'
    elif 83 <= score <= 88:
        letter_grade = 'C'
    elif 75 <= score <= 82:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade


student_dict = dict({})
with open("../DATA/testscores.dat", "r") as test_file:
    for line in test_file:
        name, score = line.rstrip().split(":")
        student_dict[name] = score

for student, score in sorted(student_dict.items(),
                             key=lambda e: e[1],
                             reverse=True
                            ):
    print("{} {}".format(student, grade(int(score))), sep="\t")
