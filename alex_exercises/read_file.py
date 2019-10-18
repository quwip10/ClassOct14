#!/usr/bin/python3
instrument_file = open("instruments.txt", "r")
instrument_list = []

for line in instrument_file:
    instrument = line.strip()
    if instrument: instrument_list.append(instrument)

instrument_file.close()

for i in instrument_list:
    print(i)

