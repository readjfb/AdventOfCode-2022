# https://adventofcode.com/2022/day/1


def day1_v1():
    with open("day1_input.txt") as f:
        data = f.read().splitlines()

    elves = [0]

    for i in data:
        if i == "":
            elves.append(0)
        else:
            elves[-1] += int(i)

    print(f"Part 1: {max(elves)}")

    elves.sort(reverse=True)

    print(f"Part 2: {sum(elves[:3])}")


def day1_v2():
    with open("day1_input.txt") as f:
        data = f.read()

    split_data = data.split("\n\n")

    elves = []

    for elf in split_data:
        elves.append(sum(int(i) for i in elf.split("\n")))

    print(f"Part 1: {max(elves)}")

    elves.sort(reverse=True)

    print(f"Part 2: {sum(elves[:3])}")


if __name__ == "__main__":
    # day1_v1()

    day1_v2()
