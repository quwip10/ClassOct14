#!/usr/bin/python3
# Exercise 15-1
# Page 338
import os.path, sys, time
from datetime import datetime

for line in sys.argv[1:]:
    if os.path.exists(line):
        epoch_time = os.path.getmtime(line)
        human_time = datetime.fromtimestamp(epoch_time)
        print(human_time.strftime('%b %d,%Y'))
