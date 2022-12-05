def day5_v1():
    with open("day5_input.txt") as f:
        puzzle_input = f.read()

    num_boxes = 9

    boxes, inputs = puzzle_input.split("\n\n")

    # Parse the boxes into a list of lists

    box_lists = [list() for i in range(num_boxes)]

    for line in boxes.splitlines()[:-1]:
        for i in range(num_boxes):
            p = (i * 4) + 1

            if p >= len(line):
                break

            character = line[p]

            if character != " ":
                box_lists[i].insert(0, character)

    commands = []

    # parse the numbers from 'move 6 from 5 to 7'
    # parse the inputs into a list of lists
    for line in inputs.splitlines():
        l = line.split(" ")

        commands.append((int(l[1]), int(l[3]), int(l[5])))

    # Create a deep copy of the box lists
    original_box_lists = [list() for i in range(9)]

    for i in range(num_boxes):
        original_box_lists[i] = box_lists[i].copy()

    # Part 1
    for command in commands:
        num, start, end = command

        start -= 1
        end -= 1

        for i in range(num):
            box_lists[end].append(box_lists[start].pop())

    # print boxes on top of each stack
    part1_output = "".join(box_lists[i][-1] for i in range(num_boxes))

    # Part 2: boxes are moved together, and stay in same order

    box_lists = original_box_lists

    for command in commands:
        num, start, end = command

        start -= 1
        end -= 1

        boxes_to_move = box_lists[start][-num:]

        # move the boxes to the end of the list
        box_lists[start] = box_lists[start][:-num]
        box_lists[end] += boxes_to_move

    # print boxes on top of each stack
    part2_output = "".join(box_lists[i][-1] for i in range(num_boxes))

    print("Part 1:", part1_output)

    print("Part 2:", part2_output)

if __name__ == "__main__":
    day5_v1()