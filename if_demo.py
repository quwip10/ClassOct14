
import sys
# python id_demo.py 30

user_input = sys.argv[1]

user_number = int(user_input)
BIG_NUMBER = 100

# ? :
warning = "Negative numbers will always be wrong" if user_number < 0 else "You are awesome"
print(warning)


if user_number > BIG_NUMBER:
    print("That is a big number")
    print("Nicely done, but not what we a looking for")
elif user_number == BIG_NUMBER:
    print("Well golly!")
    print("You are a darn good guesser")
    print("You win!!")
else:
    print("That is a fine number too.")
    print("but you could aim a little higher")
