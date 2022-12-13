# Today, I optimized a single solution for speed and code cleanliness


class RopeNode:
    def __init__(self, x, y, tail):
        self.x = x
        self.y = y
        self.tail = tail

    def perform_move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

        if not self.tail:
            return

        poten_new_tail_x = self.tail.x + (1 if self.x > self.tail.x else -1)
        poten_new_tail_y = self.tail.y + (1 if self.y > self.tail.y else -1)

        # If the move is more than one unit, it is a diagonal move
        if abs(self.y - self.tail.y) + abs(self.x - self.tail.x) > 2:
            # Move tail one step diagonally towards the new position
            self.tail.perform_move(poten_new_tail_x, poten_new_tail_y)

        elif abs(self.x - self.tail.x) > 1:
            self.tail.perform_move(poten_new_tail_x, self.tail.y)

        elif abs(self.y - self.tail.y) > 1:
            self.tail.perform_move(self.tail.x, poten_new_tail_y)

    def move_in_direction(self, direction):
        self.new_x = self.x + direction[0]
        self.new_y = self.y + direction[1]

        self.perform_move(self.new_x, self.new_y)


def perform_puzzle(puzzle_input, head_0, tail_0, head_1=None, tail_1=None):
    move_dict = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }

    tail_positions_0 = {(tail_0.x, tail_0.y)}
    tail_positions_1 = {(tail_1.x, tail_1.y)}

    for line in puzzle_input:
        dir, dist = line[0], int(line[1:])

        direction = move_dict[dir]

        for _ in range(dist):
            head_0.move_in_direction(direction)
            tail_positions_0.add((tail_0.x, tail_0.y))

            head_1.move_in_direction(direction)
            tail_positions_1.add((tail_1.x, tail_1.y))

    return len(tail_positions_0), len(tail_positions_1)


def day9():
    with open("day9_input.txt") as f:
        puzzle_input = f.readlines()

    tail_0 = RopeNode(0, 0, None)
    head_0 = RopeNode(0, 0, tail_0)

    # Part 2; the rope is now 10 units long
    # Create 10 new nodes, and have the head point to the first one and have tail
    # point to the last one.
    nodes = [RopeNode(0, 0, None) for x in range(10)]

    for i in range(9):
        nodes[i].tail = nodes[i + 1]

    head_1 = nodes[0]
    tail_1 = nodes[-1]

    part_1, part_2 = perform_puzzle(puzzle_input, head_0, tail_0, head_1, tail_1)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    day9()
