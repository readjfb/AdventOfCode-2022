import json
from prettytable import PrettyTable

# read in timing/timing.json, and print it out in a table

with open("timing/timing.json", "r") as f:
    data = json.load(f)

full_table = PrettyTable()
full_table.field_names = ["Day", "Part 1", "Part 2", "Time (s)", "Under 1s?"]

# Put a checkmark in the "Under 1s?" column if the time is under 1 second, otherwise put a cross

for day in data:
    time_value = str(round(data[day]["time"], 5))
    # pad the time value with 0s so that the table is aligned
    time_value = time_value + "0" * (7 - len(time_value))
    full_table.add_row(
        [
            int(data[day]["day"]),
            data[day]["part1"],
            data[day]["part2"],
            time_value,
            "✅" if data[day]["time"] < 1 else "❌",
        ]
    )

# Sort the table by day number
full_table.sortby = "Day"

# Save the table to a file
with open("timing/timing.txt", "w") as f:
    # f.write(str(full_table))
    # f.write("\n\n")

    f.write(full_table.get_string(fields=["Day", "Time (s)", "Under 1s?"]))
