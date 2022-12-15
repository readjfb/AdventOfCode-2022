from dataclasses import dataclass
import re
import collections

part_1_y = 2000000


@dataclass
class Sensor:
    x: int
    y: int
    closest_beacon: tuple
    distance: int


def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def num_impossible_coords(sensors, beacon_coords, y_coord):
    range_endpoints = []

    for sensor in sensors:
        y_dist = abs(sensor.y - y_coord)

        if y_dist > sensor.distance:
            continue

        x_left = sensor.x - (sensor.distance - y_dist)
        x_right = sensor.x + (sensor.distance - y_dist)

        range_endpoints.append((x_left, x_right))

    # Combine the ranges
    range_endpoints.sort(key=lambda x: x[0])

    # Find the intersection of the ranges
    new_endpoints = [range_endpoints[0]]
    i = 1
    while i < len(range_endpoints):
        if new_endpoints[-1][1] >= range_endpoints[i][0]:
            new_right = max(new_endpoints[-1][1], range_endpoints[i][1])
            new_endpoints[-1] = (new_endpoints[-1][0], new_right)
        else:
            new_endpoints.append(range_endpoints[i])
        i += 1

    num_impossible = 0

    b_list = [beacon[0] for beacon in beacon_coords if beacon[1] == y_coord]

    b_counter = collections.Counter(b_list)

    for endpoint in new_endpoints:
        num_impossible += endpoint[1] - endpoint[0] + 1

        for b, count in b_counter.items():
            if endpoint[0] <= b <= endpoint[1]:
                num_impossible -= count

    return num_impossible


def day15():
    with open("day15_input.txt", "r") as f:
        data = f.read().splitlines()

    # Parse input data; each line has two coordinates
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15

    sensors = []
    beacon_coords = set()

    for line in data:
        # Find all numeric characters including negative signs
        sensor = re.findall(r"([\d-]+)", line)

        sensor = [int(x) for x in sensor]
        sensor_x, sensor_y, beacon_x, beacon_y = sensor
        dist = man_dist(sensor_x, sensor_y, beacon_x, beacon_y)

        sensors.append(Sensor(sensor_x, sensor_y, (beacon_x, beacon_y), dist))

        beacon_coords.add((beacon_x, beacon_y))

    # Find the number of positions in a row that cannot have a sensor
    # because they are closer to a beacon than any other sensor

    part_1_solution, part_2_solution = None, None

    part_1_solution = num_impossible_coords(sensors, beacon_coords, part_1_y)

    print(f"Part 1: {part_1_solution}")

    # Part 2 - Find the only coordinate that can have a beacon
    min_coord, max_coord = 0, 4000000

    # Lines represented as
    # [x1, y1] and have slope either 1 or -1
    lines = []
    for sensor in sensors:
        # Add +y and -y line
        lines.append((sensor.x, sensor.y + sensor.distance + 1))
        lines.append((sensor.x, sensor.y - sensor.distance - 1))

    intersections = set()

    for i, line1 in enumerate(lines):
        for line2 in lines[i + 1:]:
            # Find intersection of the two lines; first line1 is the +y line
            # and line2 is the -y line
            x1, y1 = line1
            x2, y2 = line2

            x_i = (x1 + x2 + y2 - y1) / 2
            y_i = x_i - x1 + y1

            if min_coord <= x_i <= max_coord and min_coord <= y_i <= max_coord:
                intersections.add((x_i, y_i))

            # Assume that line1 is the -y line and line2 is the +y line
            x_i = (x1 + x2 - y2 + y1) / 2
            y_i = x_i - x2 + y2

            if min_coord <= x_i <= max_coord and min_coord <= y_i <= max_coord:
                intersections.add((x_i, y_i))

    # Find the intersection that is out of range of any sensor
    for inter in intersections:
        if not any(
            man_dist(inter[0], inter[1], sen.x, sen.y) <= sen.distance
            for sen in sensors
        ):
            part_2_solution = int((inter[0] * 4000000) + inter[1])
            break

    print(f"Part 2: {part_2_solution}")


if __name__ == "__main__":
    day15()
