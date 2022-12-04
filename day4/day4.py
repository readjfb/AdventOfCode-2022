def day4_v1():
    with open("day4_input.txt") as f:
        puzzle_input = f.read().splitlines()

    # Part 1

    total1, total2 = 0, 0

    for line in puzzle_input:
        f, s = line.split(",")
        # find where one range fully contains the other
        f = f.split("-")
        s = s.split("-")

        f = [int(x) for x in f]
        s = [int(x) for x in s]

        if (f[0] <= s[0] <= s[1] <= f[1]) or (s[0] <= f[0] <= f[1] <= s[1]):
            total1 += 1

        # find where the ranges overlap at all
        if (
            (f[0] <= s[0] <= f[1])
            or (s[0] <= f[0] <= s[1])
            or (f[0] <= s[1] <= f[1])
            or (s[0] <= f[1] <= s[1])
        ):
            total2 += 1

    print(f"Part 1: {total1}")
    print(f"Part 2: {total2}")


if __name__ == "__main__":
    day4_v1()
