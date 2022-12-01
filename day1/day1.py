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

if __name__ == "__main__":
    pass
day1_v1()
