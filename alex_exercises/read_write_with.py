#!/usr/bin/python3
instrument_list = []

with open("instruments.txt", "r") as instrument_file:
    for line in instrument_file:
    	instrument = line.strip()
	if instrument: instrument_list.append(instrument)


