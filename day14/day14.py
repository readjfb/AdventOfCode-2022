# Path to be used for memoization of the sand path
sand_path = [(500, 0)]


def simulate_sand(filled_coords, max_y=None):
    # Returns true if it has not out of the map
    x, y = sand_path.pop() if sand_path else (500, 0)

    while True:
        if max_y and y == max_y:
            return False
        if (x, y + 1) not in filled_coords:
            y += 1
            sand_path.append((x, y))
        elif (x - 1, y + 1) not in filled_coords:
            x -= 1
            y += 1
            sand_path.append((x, y))
        elif (x + 1, y + 1) not in filled_coords:
            x += 1
            y += 1
            sand_path.append((x, y))
        else:
            filled_coords.add((x, y))
            if sand_path:
                sand_path.pop()
                return True
            return y != 0


def day14():
    with open("day14_input.txt", "r") as f:
        data = f.read().splitlines()

    filled_coords = set()
    lowest_block = 0

    for line in data:
        coords = line.split(" -> ")

        for i in range(len(coords) - 1):
            start = coords[i].split(",")
            end = coords[i + 1].split(",")

            start_x, start_y = int(start[0]), int(start[1])
            end_x, end_y = int(end[0]), int(end[1])

            start_x, end_x = min(start_x, end_x), max(start_x, end_x)
            start_y, end_y = min(start_y, end_y), max(start_y, end_y)

            lowest_block = max(lowest_block, end_y)

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    filled_coords.add((x, y))

    part_1_solution, part_2_solution = 0, 0

    while simulate_sand(filled_coords, lowest_block):
        part_1_solution += 1

    # Part 2 simulation

    for x in range(500 - lowest_block - 3, 500 + lowest_block + 3):
        filled_coords.add((x, lowest_block + 2))

    part_2_solution = part_1_solution
    while simulate_sand(filled_coords):
        part_2_solution += 1
    part_2_solution += 1

    print(f"Part 1: {part_1_solution}")
    print(f"Part 2: {part_2_solution}")


if __name__ == "__main__":
    day14()
