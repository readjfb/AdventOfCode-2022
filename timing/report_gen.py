import json
from prettytable import PrettyTable

# read in timing/timing.json, and print it out in a table

with open("timing/timing.json", "r") as f:
    data = json.load(f)

full_table = PrettyTable()
full_table.field_names = ["Day", "Part 1", "Part 2", "Time (s)"]

for day in data:
    full_table.add_row(
        [
            data[day]["day"],
            data[day]["part1"],
            data[day]["part2"],
            round(data[day]["time"], 5),
        ]
    )

# Sort the table by day number
full_table.sortby = "Day"

# Save the table to a file
with open("timing/timing.txt", "w") as f:
    f.write(str(full_table))

    f.write("\n\n")

    f.write(full_table.get_string(fields=["Day", "Time (s)"]))
