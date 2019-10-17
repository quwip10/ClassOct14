

products = {
    101: "Zaboomafoo",
    201: "dinglehopper",
    301: "snipe",
    302: "vapoorize",
    401: "chipotle-away",
    500: "thingamajigger",
    501: "thingamajiggy",
    600: "Widget1",
    601: "Widget2",
    602: "Widget3",
}


def main():
    while True:
        try:
            user_input = input("Enter product ID: ")

            if user_input.lower() == "q" or user_input == "":
                break

            product_id = int(user_input)
            name = products[product_id]
            print("Your product:", name)

        except ValueError:
            print(
                f"'{user_input}' is not a valid prodcut id.  They are all whole numbers. Try again")
        except KeyError:
            print(f"'{user_input}' was not found in the product inventory.")
        finally:
            print("Second verse, same as the first!")


try:
    main()
except Exception as err:
    print("Unknown Exception", "You should not have been able to get this", err)
