import heapq


def djikstra_dists(grid, start_pos):
    # Create a priority queue
    pq = []
    heapq.heappush(pq, (0, start_pos))

    # Create a set of visited nodes
    visited = set()

    # Create a dictionary of distances
    distances = {}

    grid_x_len, grid_y_len = len(grid[0]), len(grid)

    while pq:
        dist, pos = heapq.heappop(pq)
        if pos in visited:
            continue
        visited.add(pos)
        distances[pos] = dist

        # Add neighbors to the queue
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_y < 0 or new_x >= grid_x_len or new_y >= grid_y_len:
                continue
            if grid[new_y][new_x] >= grid[y][x] - 1:
                heapq.heappush(pq, (dist + 1, (new_x, new_y)))

    return distances


def day12():
    with open("day12_input.txt") as f:
        instructions = f.read().splitlines()

    # Parse instructions into a matrix
    start_pos, end_pos = None, None

    grid, low_elev_positions = [], set()

    for y, line in enumerate(instructions):
        grid.append([])
        for x, c in enumerate(line):
            if c == "S":
                start_pos = (x, y)
                grid[-1].append(ord("a"))
            elif c == "E":
                end_pos = (x, y)
                grid[-1].append(ord("z"))
            else:
                grid[-1].append(ord(c))

            if grid[-1][-1] == ord("a"):
                low_elev_positions.add((x, y))

    distances = djikstra_dists(grid, end_pos)

    # part 1
    print(f"Part 1: {distances[start_pos]}")

    # part 2
    low_elev_positions = low_elev_positions.intersection(distances.keys())

    print(f"Part 2: {min(distances[pos] for pos in low_elev_positions)}")


if __name__ == "__main__":
    day12()
