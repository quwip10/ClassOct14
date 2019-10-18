import argparse
import sys

"""Square It Utillity

pass in some number ans square them

"""


parser = argparse.ArgumentParser(prog="Square It Utility")

parser.add_argument("numbers", nargs="*", type=int,
                    help="the numbers you want squared")

parser.add_argument("-d", "--debug",
                    help="Add additional debugging infomation", action="store_true")


args = parser.parse_args()


# user_number = sys.argv[1]
# number = int(user_number)

if args.debug:
    print("Debugging is on ...")

for number in args.numbers:
    if args.debug:
        print("Squaring ", number)
    answer = number ** 2
    print(answer)
