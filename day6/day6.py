def day6_v1():
    with open("day6_input.txt") as f:
        file_input = f.readlines()

    line = file_input[0]

    # Find the index of the first position with 4 unique characters sequencially

    part1_answer = None
    for i in range(4, len(line)):
        if len(set(line[i - 4 : i])) == 4:
            part1_answer = i
            break

    part2_answer = None
    for i in range(14, len(line)):
        if len(set(line[i - 14 : i])) == 14:
            part2_answer = i
            break

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    day6_v1()
