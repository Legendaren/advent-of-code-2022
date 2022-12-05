from pathlib import Path
from collections import deque
import re


def read_input():
    p = Path(__file__).with_name("day05.txt")
    with p.open() as f:
        file_text = f.read()
    return file_text.split('\n\n')


def transpose(elems):
    return list(map(list, zip(*elems)))


def parse_crates(input):
    lines = input.split('\n')[:-1]
    column_count = int(input.split('\n')[-1].rstrip()[-1])
    crate_char_width = 4*column_count - 1
    crate_rows = [line.ljust(crate_char_width)
                  for line in lines]
    crates_top_to_bottom = [[row[i] for i in range(1, len(row), 4)]
                            for row in crate_rows]
    crates_per_level = transpose(crates_top_to_bottom)
    deque_columns = [deque(crate for crate in column if crate != ' ')
                     for column in crates_per_level]
    return deque_columns


def parse_moves(input):
    pattern = re.compile('move (\d+) from (\d+) to (\d+)')
    return [list(map(int, pattern.findall(line)[0])) for line in input.split('\n')]


def solve_part1():
    crate_input, move_input = read_input()
    crate_columns = parse_crates(crate_input)
    moves = parse_moves(move_input)
    for amount, from_column, to_column in moves:
        removed_elems = [crate_columns[from_column - 1].popleft()
                         for _ in range(amount)]
        crate_columns[to_column - 1].extendleft(removed_elems)
    return ''.join([column[0] for column in crate_columns])


def solve_part2():
    crate_input, move_input = read_input()
    crate_columns = parse_crates(crate_input)
    moves = parse_moves(move_input)
    for amount, from_column, to_column in moves:
        removed_elems = reversed([crate_columns[from_column - 1].popleft()
                                  for _ in range(amount)])
        crate_columns[to_column - 1].extendleft(removed_elems)
    return ''.join([column[0] for column in crate_columns])


print(f"Part 1 answer: {solve_part1()}")
print(f"Part 2 answer: {solve_part2()}")
