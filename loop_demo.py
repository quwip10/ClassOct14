
user_number = int(input("Enter a starting number: "))

while True:
    user_number = user_number - 1

    if user_number == 4:
        continue

    if user_number % 2 == 0:
        print("Even Number")
    else:
        print("Odd number")

    print("The Number: ", user_number)
