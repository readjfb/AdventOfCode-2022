import re
import math
from collections import deque

class Monkey():
    def __init__(self):
        self.number = None
        self.items = deque()
        self.operation = None
        self.test = None
        self.true_target_num = None
        self.false_target_num = None
        self.true_target = None
        self.false_target = None

        self.num_inspected = 0

    def perform_turn(self, division_factor=None, modulo_factor=None):
        while self.items:
            item = self.items.popleft()
            new_item = self.operation(item)

            if division_factor:
                new_item = new_item // division_factor

            if modulo_factor:
                new_item = new_item % modulo_factor

            if self.test(new_item):
                self.true_target.items.append(new_item)
            else:
                self.false_target.items.append(new_item)

            self.num_inspected += 1

    def __repr__(self) -> str:
        return f"Monkey {self.number} holding {self.items}"

"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0
"""
def parse_note(note):
    monkey_num = int(re.search(r'Monkey (\d+):', note).group(1))

    items = re.search(r'Starting items: (.*)', note).group(1).split(', ')
    items = [int(item) for item in items]

    # Parse and convert operation to a lambda function
    operation = re.search(r'Operation: (.*)', note).group(1)
    operation = operation.replace('new = old', 'lambda old: old')
    operation = eval(operation)

    test_divisor = int(re.search(r'Test: divisible by (\d+)', note).group(1))

    test = lambda old: old % test_divisor == 0

    true_target = int(re.search(r'If true: throw to monkey (\d+)', note).group(1))
    false_target = int(re.search(r'If false: throw to monkey (\d+)', note).group(1))

    return monkey_num, items, operation, test, true_target, false_target, test_divisor

def day11():
    with open('day11_input.txt') as f:
        lines = f.read()

    monkey_notes = lines.split("\n\n")

    monkeys = []

    for note in monkey_notes:
        parsed = parse_note(note)

        monkey = Monkey()
        monkey.number = parsed[0]

        for items in parsed[1]:
            monkey.items.append(items)

        monkey.operation = parsed[2]
        monkey.test = parsed[3]
        monkey.true_target_num = parsed[4]
        monkey.false_target_num = parsed[5]

        monkeys.append(monkey)

    for monkey in monkeys:
        monkey.true_target = monkeys[monkey.true_target_num]
        monkey.false_target = monkeys[monkey.false_target_num]

    num_rounds = 20

    for i in range(num_rounds):
        for monkey in monkeys:
            monkey.perform_turn(division_factor=3)

    # Find the two most active monkeys
    activity = [monkey.num_inspected for monkey in monkeys]
    activity.sort(reverse=True)

    part_1 = activity[0] * activity[1]

    print(f"Part 1: {part_1}")

    # Part 2
    # Restart the monkeys
    mod_factor = 1

    monkeys = []
    for note in monkey_notes:
        parsed = parse_note(note)

        monkey = Monkey()
        monkey.number = parsed[0]

        for items in parsed[1]:
            monkey.items.append(items)

        monkey.operation = parsed[2]
        monkey.test = parsed[3]
        monkey.true_target_num = parsed[4]
        monkey.false_target_num = parsed[5]

        monkeys.append(monkey)

        mod_factor = math.lcm(mod_factor, parsed[6])

    for monkey in monkeys:
        monkey.true_target = monkeys[monkey.true_target_num]
        monkey.false_target = monkeys[monkey.false_target_num]

    num_rounds = 10000

    for i in range(num_rounds):
        for monkey in monkeys:
            monkey.perform_turn(division_factor=1, modulo_factor=mod_factor)

    # Find the two most active monkeys
    activity = [monkey.num_inspected for monkey in monkeys]
    activity.sort(reverse=True)

    part_2 = activity[0] * activity[1]

    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    day11()

