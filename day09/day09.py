from pathlib import Path


def read_input():
    p = Path(__file__).with_name("day09.txt")
    with p.open() as f:
        lines = (line.rstrip().split() for line in f.readlines())
        return [(direction, int(steps)) for direction, steps in lines]


direction_to_coords = {
    'L': (-1, 0),
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1)
}


def move_positions(head_pos, move):
    x, y = head_pos
    direction, steps = move
    add_x, add_y = direction_to_coords[direction]
    for _ in range(steps):
        x += add_x
        y += add_y
        yield x, y


def adjacent(head_pos, tail_pos):
    x, y = head_pos
    adjacent_pos_to_head = set((i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2))
    return tail_pos in adjacent_pos_to_head


def move_towards_head(head_pos, knot_pos):
    head_x, head_y = head_pos
    tail_x, tail_y = knot_pos
    pos_x = tail_x + 1 if head_x > tail_x else tail_x - 1
    pos_y = tail_y + 1 if head_y > tail_y else tail_y - 1
    if head_x == tail_x:
        return tail_x, pos_y
    elif head_y == tail_y:
        return pos_x, tail_y
    else:
        return pos_x, pos_y


def solve_knots(n):
    moves = read_input()
    knots = [(0, 0) for _ in range(n)]
    tail_visited_pos = {(0, 0)}
    for move in moves:
        for p in move_positions(knots[0], move):
            knots[0] = p
            for i in range(1, len(knots)):
                if not adjacent(knots[i - 1], knots[i]):
                    knots[i] = move_towards_head(knots[i - 1], knots[i])
            tail_visited_pos.add(knots[-1])
    return len(tail_visited_pos)


print(f"Part 1 answer: {solve_knots(2)}")
print(f"Part 2 answer: {solve_knots(10)}")
