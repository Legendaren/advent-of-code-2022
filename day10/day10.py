from pathlib import Path
import re


class CPU:
    addx_pattern = re.compile('^addx (-?\d+)$')
    noop_pattern = re.compile('^noop$')
    required_cycles = {
        'addx': 2,
        'noop': 1
    }

    def __init__(self, instructions):
        self.instructions = instructions
        self.instruction_counter = 0
        self.current_instruction_cycle = 0
        self.x_reg = 1
        self.cycle = 1
        self.signal_strengths = [self.x_reg * self.cycle]

    def signal_strength(self):
        return self.x_reg * self.cycle

    def current_instruction(self):
        current_inst = self.instructions[self.instruction_counter]
        if match := self.addx_pattern.findall(current_inst):
            return "addx", int(match[0])
        elif self.noop_pattern.findall(current_inst):
            return "noop", None

    def execute(self):
        self.current_instruction_cycle += 1
        op, arg = self.current_instruction()
        if self.current_instruction_cycle >= self.required_cycles[op]:
            if op == 'addx':
                self.x_reg += arg
            self.current_instruction_cycle = 0
            self.instruction_counter += 1

    def is_finished(self):
        return self.instruction_counter >= len(self.instructions)

    def tick(self):
        if self.is_finished():
            return
        self.execute()
        self.cycle += 1
        self.signal_strengths.append(self.signal_strength())


def read_input():
    p = Path(__file__).with_name("day10.txt")
    with p.open() as f:
        return [line.rstrip() for line in f.readlines()]


def solve_part1():
    instructions = read_input()
    cpu = CPU(instructions)
    while not cpu.is_finished():
        cpu.tick()
    return sum(cpu.signal_strengths[19:220:40])


def solve_part2():
    crt = []
    crt_line = []
    pixel_pos = 0
    instructions = read_input()
    cpu = CPU(instructions)
    while not cpu.is_finished():
        sprite_pos = range(cpu.x_reg - 1, cpu.x_reg + 2)
        crt_line.append('#' if pixel_pos in sprite_pos else '.')
        pixel_pos += 1
        if pixel_pos > 39:
            pixel_pos = 0
            crt.append(''.join(crt_line))
            crt_line.clear()
        cpu.tick()
    return '\n'.join(crt)


print(f"Part 1 answer: {solve_part1()}")
print(f"Part 2 answer: \n{solve_part2()}")
