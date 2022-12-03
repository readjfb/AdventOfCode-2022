def day3_v1():
    with open("day3_input.txt") as f:
        puzzle_input = f.read().splitlines()

    # lowercase priorities are 1-26 a-z
    # uppercase priorities are 27-52 A-Z

    # Part 1
    score = 0

    for line in puzzle_input:
        f, s = line[: len(line) // 2], line[len(line) // 2 :]

        f_set = set(x for x in f)
        s_set = set(x for x in s)

        matching = f_set.intersection(s_set)

        for char in matching:
            score += ord(char) - 96 if char.islower() else ord(char) - 38

    print(f"Part 1: {score}")

    # part 2

    # loop through groups of 3 lines

    i = 0
    pt2_score = 0
    while i < len(puzzle_input):
        f, s, t = puzzle_input[i], puzzle_input[i + 1], puzzle_input[i + 2]

        f_set = set(x for x in f)
        s_set = set(x for x in s)
        t_set = set(x for x in t)

        matching = f_set.intersection(s_set, t_set)

        for char in matching:
            pt2_score += ord(char) - 96 if char.islower() else ord(char) - 38

        i += 3

    print(f"Part 2: {pt2_score}")


if __name__ == "__main__":
    day3_v1()
