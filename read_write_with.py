
# with provides a context that can be automaticall closed
# when the block is over

with open("instruments.txt", "r") as instrument_file:

    instrument_list = []
    for line in instrument_file:
        instrument = line.strip()
        instrument_list.append(instrument)


for i in instrument_list:
    print(i)


new_instrument = input("Add an instrument: ")

# if new_instrument not in instrument_list:
#     instrument_list.append(new_instrument)
#     with open("instruments.txt", "w") as instrument_file:
#         for instrument in instrument_list:
#             instrument_file.write(instrument)
#             instrument_file.write("\n")

#     print("File Saved")
# else:
#     print("** already in list. Skipping. **")


if new_instrument not in instrument_list:
    instrument_list.append(new_instrument)

    # generator to append a \n to the end of every instrument
    lines = (
        i + "\n"
        for i in instrument_list
    )

    with open("instruments.txt", "w") as instrument_file:
        instrument_file.writelines(lines)

    print("File Saved")
else:
    print("** already in list. Skipping. **")
