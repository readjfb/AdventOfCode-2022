def day8_v1():
    # INITIAL ATTEMPT- Brute force solution, with room to optimize for sure

    # Find trees that are not externally visible
    with open("day8_input.txt") as f:
        file_input = f.readlines()

    # Part 1
    # parse the input into a grid
    maximum_height = 0
    tree_grid = []
    for line in file_input:
        tree_grid.append([int(x) for x in line.strip()])
        maximum_height = max(maximum_height, max(tree_grid[-1]))

    valid_grid = [[True for x in range(len(tree_grid[0]))] for y in range(len(tree_grid))]

    # Check for visibility from left to right
    for y in range(len(tree_grid)):
        max_height = tree_grid[y][0]
        valid_grid[y][0] = False
        for x in range(1, len(tree_grid[0])):
            if tree_grid[y][x] > max_height:
                max_height = tree_grid[y][x]
                valid_grid[y][x] = False

    # Check for visibility from right to left
    for y in range(len(tree_grid)):
        max_height = tree_grid[y][-1]
        valid_grid[y][-1] = False
        for x in range(len(tree_grid[0]) - 2, -1, -1):
            if tree_grid[y][x] > max_height:
                max_height = tree_grid[y][x]
                valid_grid[y][x] = False

    # Check for visibility from top to bottom
    for x in range(len(tree_grid[0])):
        max_height = tree_grid[0][x]
        valid_grid[0][x] = False
        for y in range(1, len(tree_grid)):
            if tree_grid[y][x] > max_height:
                max_height = tree_grid[y][x]
                valid_grid[y][x] = False

    # Check for visibility from bottom to top
    for x in range(len(tree_grid[0])):
        max_height = tree_grid[-1][x]
        valid_grid[-1][x] = False
        for y in range(len(tree_grid) - 2, -1, -1):
            if tree_grid[y][x] > max_height:
                max_height = tree_grid[y][x]
                valid_grid[y][x] = False

    # Count the number of visible trees
    visible_trees = 0
    for y in range(len(valid_grid)):
        for x in range(len(valid_grid[0])):
            if not valid_grid[y][x]:
                visible_trees += 1

    print(f"Part 1: {visible_trees}")

    # Part 2
    # Find the farthest view distance in each direction for each tree
    highest_scenic_view = 0

    for y in range(1, len(valid_grid) - 1):
        for x in range(1, len(valid_grid[0]) - 1):
            i = 1
            # Check visibility to the left first
            i = 1
            while x - i > 0:
                if tree_grid[y][x - i] >= tree_grid[y][x]:
                    break
                i += 1
            view_L = i

            # Check visibility to the right
            i = 1
            while x + i < len(valid_grid[0]) - 1:
                if tree_grid[y][x + i] >= tree_grid[y][x]:
                    break
                i += 1
            view_R = i

            # Check visibility to the top
            i = 1
            while y - i > 0:
                if tree_grid[y - i][x] >= tree_grid[y][x]:
                    break
                i += 1
            view_T = i

            # Check visibility to the bottom
            i = 1
            while y + i < len(valid_grid) - 1:
                if tree_grid[y + i][x] >= tree_grid[y][x]:
                    break
                i += 1
            view_B = i

            new_score = view_L * view_R * view_T * view_B

            highest_scenic_view = max(highest_scenic_view, new_score)

    print(f"Part 2: {highest_scenic_view}")


def day8_v2():
    with open("day8_input.txt") as f:
        file_input = f.readlines()

    # Part 1
    # parse the input into a grid
    maximum_height = 0
    tree_grid = []
    for line in file_input:
        tree_grid.append([int(x) for x in line.strip()])
        maximum_height = max(maximum_height, max(tree_grid[-1]))

    highest_scenic_view = 0
    externally_visible_trees = (len(tree_grid) * 2) + (len(tree_grid[0]) * 2) - 4

    for y in range(1, len(tree_grid) - 1):
        for x in range(1, len(tree_grid[0]) - 1):
            new_score = 1

            flag = False

            # Check visibility to the left first
            i = 1
            while x - i > 0:
                if tree_grid[y][x - i] >= tree_grid[y][x]:
                    break
                i += 1
            else:
                flag |= tree_grid[y][0] < tree_grid[y][x]
            new_score *= i

            # Check visibility to the right
            i = 1
            while x + i < len(tree_grid[0]) - 1:
                if tree_grid[y][x + i] >= tree_grid[y][x]:
                    break
                i += 1
            else:
                flag |= tree_grid[y][-1] < tree_grid[y][x]
            new_score *= i

            # Check visibility to the top
            i = 1
            while y - i > 0:
                if tree_grid[y - i][x] >= tree_grid[y][x]:
                    break
                i += 1
            else:
                flag |= tree_grid[0][x] < tree_grid[y][x]
            new_score *= i

            # Check visibility to the bottom
            i = 1
            while y + i < len(tree_grid) - 1:
                if tree_grid[y + i][x] >= tree_grid[y][x]:
                    break
                i += 1
            else:
                flag |= tree_grid[-1][x] < tree_grid[y][x]
            new_score *= i

            externally_visible_trees += flag

            highest_scenic_view = max(highest_scenic_view, new_score)

    print(f"Part 1: {externally_visible_trees}")
    print(f"Part 2: {highest_scenic_view}")


if __name__ == "__main__":
    # day8_v1()

    day8_v2()
