

instrument_file = open("./data/instruments.txt", "r")

instrument_list = []
for line in instrument_file:
    instrument = line.strip()
    instrument_list.append(instrument)

instrument_file.close()

for i in instrument_list:
    print(i)


new_instrument = input("Add an instrument: ")

if new_instrument not in instrument_list:
    instrument_list.append(new_instrument)
    instrument_file = open("./data/instruments.txt", "w")
    for instrument in instrument_list:
        instrument_file.write(instrument)
        instrument_file.write("\n")

    instrument_file.close()


else:
    print("** already in list. Skipping. **")
