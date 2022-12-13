def day10():
    with open("day10_input.txt") as f:
        puzzle_input = f.read().splitlines()

    cycle_number = 1
    register_x = 1
    pc = 0

    cycle_delay = 0

    instruction = None

    capture_times = [20, 60, 100, 140, 180, 220]

    capture_values = []

    image_stream = ""

    ON, OFF = "#", " "
    line_length = 40

    while pc < len(puzzle_input):
        if cycle_delay == 0:
            # Begin a new instruction cycle
            instruction = puzzle_input[pc].split(" ")

            if instruction[0] == "noop":
                cycle_delay = 1
            else:
                cycle_delay = 2

        # DURING CYCLE
        if cycle_number in capture_times:
            capture_values.append(register_x)

        sprite_position = (register_x % line_length) - 1

        if sprite_position < (cycle_number % line_length) < sprite_position + 4:
            image_stream += ON
        else:
            image_stream += OFF

        # END DURING CYCLE

        cycle_delay -= 1
        cycle_number += 1

        if cycle_delay == 0:
            pc += 1

            if instruction[0] == "addx":
                register_x += int(instruction[1])

    part_1 = 0

    for time, value in zip(capture_times, capture_values):
        part_1 += time * value

    print(f"Part 1: {part_1}")

    # Split the image stream into lines
    for i in range(len(image_stream) // line_length):
        print(image_stream[i * line_length : (i + 1) * line_length])

    # part 2 from inspection of the image
    print(f"Part 2: inspection")

if __name__ == "__main__":
    day10()
