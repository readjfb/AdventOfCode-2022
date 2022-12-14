import os
import time
import subprocess
import re
import json

"""
Code to time each day's code for Advent of Code 2022
Each day's code is in a separate file, in it's own directory
Structured as AdventOfCode-2022/dayx/dayx.py
Each day's code is run 10 times, and the average time is calculated
Each line outputted for each day is in the format:
Part 1: x.xxxxxx
Part 2: x.xxxxxx

Intended to be run from the root directory of the repo
"""

# Get a list of all the directories in the current directory
# Each directory is a day's code
days = [i for i in os.listdir() if os.path.isdir(i) and i.startswith("day")]

# print days
data = {}

# Loop through each day's code
for day in sorted(days, reverse=True):
    print(f"Timing {day}")
    # Get the day number from the directory name
    day_num = re.findall(r"day(\d+)", day)[0]

    # Get the file name
    file_name = f"day{day_num}.py"

    # Get the path to the file
    file_path = os.path.join(day, file_name)

    # CD into the day's directory
    os.chdir(day)

    # Run the code 10 times, and calculate the average time
    times = []
    for i in range(10):
        start = time.time()
        output = subprocess.run(["python", file_name], capture_output=True, text=True)
        end = time.time()
        times.append(end - start)
    min_time = min(times)

    # Get the output from the code
    output = output.stdout
    part1 = re.search(r"Part 1: (.*)", output).group(1)
    part2 = re.search(r"Part 2: (.*)", output).group(1)

    # Print the output
    print(f"\tPart 1: {part1}", end="\t")
    print(f"Part 2: {part2}", end="\t")
    print(f"Minimum time for day {day_num}: {min_time} seconds")

    # Add the output to the data dictionary
    data[day] = {"time": min_time, "part1": part1, "part2": part2, "day": day_num}

    # CD back to the main directory
    os.chdir("..")

# Open the timing.json file
# This file contains the data from previous runs
update_data = {}

if os.path.exists("timing/timing.json"):
    with open("timing/timing.json", "r") as f:
        update_data = json.load(f)

# Add the new data to the previous data; don't overwrite previous data
for day in data.keys():
    if day not in update_data:
        update_data[day] = data[day]
        continue

    if data[day]["time"] < update_data[day]["time"]:
        update_data[day] = data[day]

# Save the data to a file
with open("timing/timing.json", "w") as f:
    json.dump(data, f, indent=4)
