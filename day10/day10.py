from pathlib import Path
import re


class CPU:
    def __init__(self):
        self.x_reg = 1
        self.cycle = 1
        self.signal_strengths = [self.x_reg * self.cycle]

    def signal_strength(self):
        return self.x_reg * self.cycle

    def perform_cycle(self, n=1):
        for _ in range(n):
            self.cycle += 1
            self.signal_strengths.append(self.signal_strength())

    def addx(self, n):
        self.perform_cycle()
        self.x_reg += n
        self.perform_cycle()

    def noop(self):
        self.perform_cycle()


def read_input():
    p = Path(__file__).with_name("day10.txt")
    with p.open() as f:
        return [line.rstrip() for line in f.readlines()]


def solve_part1():
    instructions = read_input()
    addx_pattern = re.compile('^addx (-?\d+)$')
    noop_pattern = re.compile('^noop$')

    cpu = CPU()
    for inst in instructions:
        if match := addx_pattern.findall(inst):
            cpu.addx(int(match[0]))
        elif noop_pattern.findall(inst):
            cpu.noop()
    return sum(cpu.signal_strengths[19:220:40])


print(f"Part 1 answer: {solve_part1()}")
