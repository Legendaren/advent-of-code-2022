from pathlib import Path
from collections import deque
import re
import math


class Monkey:
    def __init__(self,
                 n,
                 starting_items,
                 operator_func,
                 divisor,
                 if_true_monkey,
                 if_false_monkey):
        self.n = n
        self.items = starting_items
        self.operator_func = operator_func
        self.divisor = divisor
        self.inspected_items_count = 0
        self.if_true_monkey = if_true_monkey
        self.if_false_monkey = if_false_monkey

    def throw_to(self, is_divisible):
        return self.if_true_monkey if is_divisible else self.if_false_monkey

    def popleft(self):
        self.inspected_items_count += 1
        return self.items.popleft()

    def append(self, item):
        self.items.append(item)


def parse_operation(op_str):
    operand1, operator, operand2 = op_str.split()
    if operator == '+':
        if operand2 == 'old':
            return lambda old: old + old
        else:
            return lambda old: old + int(operand2)
    elif operator == '*':
        if operand2 == 'old':
            return lambda old: old * old
        else:
            return lambda old: old * int(operand2)
    return None


def read_input():
    p = Path(__file__).with_name("day11.txt")
    with p.open() as f:
        lines = f.read().split('\n\n')
        lines = [line.split('\n') for line in lines]

    monkey_pattern = re.compile(r'Monkey (\d+)')
    starting_items_pattern = re.compile(r'(\d+)')
    operation_pattern = re.compile(r'Operation: new = (.+)')
    test_pattern = re.compile(r'Test: divisible by (\d+)')
    if_true_pattern = re.compile(r'If true: throw to monkey (\d+)')
    if_false_pattern = re.compile(r'If false: throw to monkey (\d+)')

    monkeys = []
    for line in lines:
        n = int(monkey_pattern.findall(line[0])[0])
        starting_items = deque(int(item) for item in starting_items_pattern.findall(line[1]))
        operator_func = parse_operation(operation_pattern.findall(line[2])[0])
        divisor = int(test_pattern.findall(line[3])[0])
        true_monkey = int(if_true_pattern.findall(line[4])[0])
        false_monkey = int(if_false_pattern.findall(line[5])[0])
        monkeys.append(Monkey(n, starting_items, operator_func, divisor, true_monkey, false_monkey))
    return monkeys


def solve_part1():
    monkeys = read_input()
    for round in range(20):
        for monkey in monkeys:
            while monkey.items:
                worry_level = monkey.popleft()
                new_worry_level = monkey.operator_func(worry_level)
                new_worry_level //= 3
                is_divisible = new_worry_level % monkey.divisor == 0
                monkeys[monkey.throw_to(is_divisible)].append(new_worry_level)
    sorted_by_inspection_counts = sorted(m.inspected_items_count for m in monkeys)
    count1, count2 = sorted_by_inspection_counts[-2:]
    return count1 * count2


def solve_part2():
    monkeys = read_input()
    least_common_divisor = math.lcm(*(m.divisor for m in monkeys))
    for round in range(10000):
        for monkey in monkeys:
            while monkey.items:
                worry_level = monkey.popleft()
                new_worry_level = monkey.operator_func(worry_level)
                new_worry_level %= least_common_divisor
                is_divisible = new_worry_level % monkey.divisor == 0
                monkeys[monkey.throw_to(is_divisible)].append(new_worry_level)
    sorted_by_inspection_counts = sorted(m.inspected_items_count for m in monkeys)
    count1, count2 = sorted_by_inspection_counts[-2:]
    return count1 * count2


print(f"Part 1 answer: {solve_part1()}")
print(f"Part 2 answer: {solve_part2()}")
