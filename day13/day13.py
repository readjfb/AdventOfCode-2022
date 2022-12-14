import functools


def compare(a, b):
    if type(a) == type(b) == int:
        if a > b:
            return -1
        elif a < b:
            return 1
        else:
            return 0

    if type(a) == type(b) == list:
        length_a, length_b = len(a), len(b)
        i = 0
        while i < length_a:
            if i >= length_b:
                return -1

            r = compare(a[i], b[i])
            if r != 0:
                return r

            i += 1

        if length_a == length_b:
            return 0
        else:
            return 1

    if type(a) == int and type(b) == list:
        return compare([a], b)

    if type(a) == list and type(b) == int:
        return compare(a, [b])

    print("Error: compare() does not support types", type(a), "and", type(b))


def day13_v1():
    """
    Initial method of solving the problem - Uses a bubble sort to sort the list

    Not very efficient, but it works
    """
    with open("day13_input.txt", "r") as f:
        data = f.read()

    pairs = [pair.split("\n") for pair in data.split("\n\n")]

    pairs = [(eval(pair[0]), eval(pair[1])) for pair in pairs]

    index_sum_in_order = 0

    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) >= 0:
            index_sum_in_order += i + 1

    print("Part 1:", index_sum_in_order)

    # Move all pairs into a single list
    full_pairs = [pair for pair in pairs for pair in pair]
    full_pairs += [[[2]], [[6]]]

    done_flag = False

    len_full_pairs = len(full_pairs)

    while not done_flag:
        i = 0
        done_flag = True
        while i < len_full_pairs - 1:
            # if comparason is false, swap the two elements
            if compare(full_pairs[i], full_pairs[i + 1]) < 0:
                full_pairs[i], full_pairs[i + 1] = full_pairs[i + 1], full_pairs[i]
                done_flag = False
                i += 2
            else:
                i += 1

    # Find the index of [[2]]
    index_0 = full_pairs.index([[2]]) + 1
    index_1 = full_pairs.index([[6]]) + 1

    part_2 = index_0 * index_1

    print("Part 2:", part_2)


def day13_v2():
    """
    Second method of solving the problem - Uses the built-in sorted() function
    with the functools.cmp_to_key() function

    Runs around 5-10x faster than the first method, using 35x fewer comparisons
    (406,007 -> 11,568)
    """
    with open("day13_input.txt", "r") as f:
        data = f.read()

    pairs = [pair.split("\n") for pair in data.split("\n\n")]
    pairs = [(eval(pair[0]), eval(pair[1])) for pair in pairs]

    index_sum_in_order = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) >= 0:
            index_sum_in_order += i + 1

    print("Part 1:", index_sum_in_order)

    # Move all pairs into a single list
    full_pairs = [pair for pair in pairs for pair in pair]
    full_pairs += [[[2]], [[6]]]

    # Sort the list
    full_pairs = sorted(full_pairs, key=functools.cmp_to_key(compare), reverse=True)

    index_0 = full_pairs.index([[2]]) + 1
    index_1 = full_pairs.index([[6]]) + 1

    part_2 = index_0 * index_1

    print("Part 2:", part_2)


if __name__ == "__main__":
    day13_v2()
