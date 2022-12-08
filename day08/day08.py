from pathlib import Path


def read_input():
    p = Path(__file__).with_name("day08.txt")
    with p.open() as f:
        return [[int(n) for n in line.rstrip()] for line in f.readlines()]


def is_on_edge(grid, pos):
    row, col = pos
    return row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1


def tree_iterator(grid, start_pos, step):
    current_tree_pos = start_pos
    while not is_on_edge(grid, current_tree_pos):
        new_row = current_tree_pos[0] + step[0]
        new_col = current_tree_pos[1] + step[1]
        current_tree_pos = new_row, new_col
        yield current_tree_pos


def interior_trees(grid):
    return [(r, c) for r in range(1, len(grid) - 1) for c in range(1, len(grid[r]) - 1)]


def is_visible_from_outside_grid(grid, pos):
    left = tree_iterator(grid, pos, (0, -1))
    right = tree_iterator(grid, pos, (0, 1))
    up = tree_iterator(grid, pos, (-1, 0))
    down = tree_iterator(grid, pos, (1, 0))
    return any(all_trees_shorter(grid, pos, trees) for trees in [left, right, up, down])


def all_trees_shorter(grid, tree, other_trees):
    row, col = tree
    height = grid[row][col]
    for ot_row, ot_col in other_trees:
        ot_height = grid[ot_row][ot_col]
        if ot_height >= height:
            return False
    return True


def viewing_distance(grid, start_pos, step):
    height = grid[start_pos[0]][start_pos[1]]
    tree_count = 0
    for row, col in tree_iterator(grid, start_pos, step):
        current_height = grid[row][col]
        tree_count += 1
        if current_height >= height:
            break

    return tree_count


def scenic_score(grid, pos):
    left_count = viewing_distance(grid, pos, (0, -1))
    right_count = viewing_distance(grid, pos, (0, 1))
    up_count = viewing_distance(grid, pos, (-1, 0))
    down_count = viewing_distance(grid, pos, (1, 0))
    return left_count * right_count * up_count * down_count


def solve_part1():
    grid = read_input()
    visible_trees_exterior = 2 * len(grid) + 2 * (len(grid) - 2)
    visible_trees_interior = 0
    for pos in interior_trees(grid):
        if is_visible_from_outside_grid(grid, pos):
            visible_trees_interior += 1
    return visible_trees_exterior + visible_trees_interior


def solve_part2():
    grid = read_input()
    return max(scenic_score(grid, pos) for pos in interior_trees(grid))


print(f"Part 1 answer: {solve_part1()}")
print(f"Part 2 answer: {solve_part2()}")
