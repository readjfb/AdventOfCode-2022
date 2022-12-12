from dataclasses import dataclass

@dataclass
class directory:
    name: str
    size: int
    children: dict

with open("day7_input.txt") as f:
    file_input = f.readlines()

current_dir = None
root_dir = None

recur_stack = []

all_dirs = []

for line in file_input:
    line = line.strip().split(" ")

    if line[0] == "$":
        # Command
        if line[1] == "cd":
            # CD Command
            if not root_dir:
                root_dir = directory(line[2], 0, {})
                current_dir = root_dir
                all_dirs.append(root_dir)
            else:
                if line[2] == "..":
                    # Go up
                    current_dir = recur_stack.pop()
                elif line[2] in current_dir.children:
                    recur_stack.append(current_dir)
                    current_dir = current_dir.children[line[2]]
                else:
                    current_dir.children[line[2]] = directory(line[2], 0, {})
                    all_dirs.append(current_dir.children[line[2]])

                    recur_stack.append(current_dir)
                    current_dir = current_dir.children[line[2]]

        elif line[1] == "ls":
            pass
        continue

    # In an LS block
    if line[0] == "dir":
        # Directory
        current_dir.children[line[1]] = directory(line[1], 0, {})
        all_dirs.append(current_dir.children[line[1]])
    else:
        file_size = int(line[0])
        current_dir.size += file_size

# Recursively calculate sizes
def calc_size(dir):
    for child in dir.children.values():
        calc_size(child)
        dir.size += child.size

calc_size(root_dir)

# Find the sum of the outermost directories with size <= 100000
def find_outermost_p1(dir):
    if dir.size > 100000:
        return sum([find_outermost_p1(child) for child in dir.children.values()])
    else:
        return dir.size + sum([find_outermost_p1(child) for child in dir.children.values()])

# print the structure
def print_structure(dir, depth=0):
    print("  "*depth, dir.name, dir.size)
    for child in dir.children.values():
        print_structure(child, depth+1)

# print_structure(root_dir)

print(f"Part 1: {find_outermost_p1(root_dir)}")

# Part 2
update_size = 30000000
total_size = 70000000

free_space = total_size - root_dir.size

removal_size = update_size - free_space

part_2 = min([dir.size for dir in all_dirs if dir.size > removal_size])

print(f"Part 2: {part_2}")
