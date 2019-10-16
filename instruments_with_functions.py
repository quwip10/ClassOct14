
import sys


instrument_path = "./data/instruments.txt"


def main():

    global instrument_path  # I will change a global variable

    if len(sys.argv) > 1:
        print("writing to ...", sys.argv[1])
        instrument_path = sys.argv[1]

    # save_instruments(["kazoo", "banjo", "flute"])
    original_instruments = get_instruments()
    new_instrument = input("Add a new Instruments: ")

    valid, errors = is_valid_instrument(new_instrument)

    if not valid:
        for error in errors:
            print(error)
        return

    if new_instrument not in original_instruments:
        new_collection = original_instruments + [new_instrument]
        save_instruments(new_collection)
        print("New instrument added")
    else:
        print("Already there. No save")


def get_instruments():
    with open(instrument_path) as instrument_in:
        instruments = [
            instrument.lower().strip()  # select/transform
            for instrument in instrument_in  # from/datasource
            # where/filter
        ]
        return instruments


def save_instruments(instruments):
    prepared_instruments = (
        i + "\n"
        for i in instruments
    )
    with open(instrument_path, "w") as instrument_out:
        instrument_out.writelines(prepared_instruments)


def my_print(*value, prefix="rob says...", **additional):
    for v in value:
        print(prefix, v)
    for k, v in additional.items():
        print(k, v)


def is_valid_instrument(instrument):
    bad_instruments = ["theramin", "elderberries", "didgeridoo"]
    errors = []
    if len(instrument) == 0:
        errors.append("Instrument must have a name")

    if not instrument.islower():
        errors.append("Instrument names must be all lower cased")

    if instrument.lower() in bad_instruments:
        errors.append("That instrument is not allowed")

    if len(errors) > 0:
        return (False, errors)
    else:
        return (True, None)


main()  # calling the main functions
