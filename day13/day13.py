from pathlib import Path
from itertools import zip_longest
from functools import cmp_to_key


def read_input():
    p = Path(__file__).with_name("day13.txt")
    with p.open() as f:
        lines = (line.rstrip() for line in f.readlines())
        lines = list(filter(lambda s: s, lines))
        pairs = []
        for i in range(0, len(lines), 2):
            p1, p2 = lines[i:i + 2]
            pairs.append((eval(p1), eval(p2)))
        return pairs


def in_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0

    if isinstance(left, list) and isinstance(right, list):
        for a, b in zip_longest(left, right):
            if a is None:
                return 1
            if b is None:
                return -1
            res = in_order(a, b)
            if res != 0:
                return res
        return 0

    if isinstance(left, int) and isinstance(right, list):
        return in_order([left], right)

    if isinstance(left, list) and isinstance(right, int):
        return in_order(left, [right])


def solve_part1(pairs):
    indices = []
    for i, (p1, p2) in enumerate(pairs, start=1):
        res = in_order(p1, p2)
        if res == 1:
            indices.append(i)
    return sum(indices)


def solve_part2(pairs):
    div_pkg1 = [[2]]
    div_pkg2 = [[6]]
    extended_pairs = pairs + [(div_pkg1, div_pkg2)]
    flattened_pairs = list(sum(extended_pairs, ()))
    sorted_pairs = sorted(flattened_pairs, key=cmp_to_key(in_order), reverse=True)
    div_pkg1_index = sorted_pairs.index(div_pkg1) + 1
    div_pkg2_index = sorted_pairs.index(div_pkg2) + 1
    return div_pkg1_index * div_pkg2_index


input_pairs = read_input()
print(f"Part 1 answer: {solve_part1(input_pairs)}")
print(f"Part 2 answer: {solve_part2(input_pairs)}")
