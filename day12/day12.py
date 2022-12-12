from pathlib import Path
import string
import networkx as nx

elevation = dict((value, i) for i, value in enumerate(string.ascii_lowercase))
elevation['S'] = elevation['a']
elevation['E'] = elevation['z']


def in_bounds(g, row, col):
    return 0 <= row < len(g) and 0 <= col < len(g[0])


def char_pos(grid, char):
    x = [x for x in grid if char in x][0]
    return grid.index(x), x.index(char)


def all_char_pos(grid, char_to_find):
    positions = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == char_to_find:
                positions.append((r, c))
    return positions


def neighbor_pos(g, row, col):
    up = (row - 1, col)
    right = (row, col + 1)
    down = (row + 1, col)
    left = (row, col - 1)
    return [p for p in [up, right, down, left] if in_bounds(g, *p)]


def generate_graph(grid):
    g = nx.DiGraph()
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            g.add_node((r, c), elevation=elevation[char])

    for node in g.nodes:
        node_elevation = g.nodes[node]['elevation']
        for neighbor in neighbor_pos(grid, *node):
            neighbor_elevation = g.nodes[neighbor]['elevation']
            if node_elevation >= neighbor_elevation or neighbor_elevation - node_elevation == 1:
                g.add_edge(node, neighbor)
    return g


def read_input():
    p = Path(__file__).with_name("day12.txt")
    with p.open() as f:
        return [line.rstrip() for line in f.readlines()]


def solve_part1(grid, graph):
    shortest_path = nx.shortest_path(graph, source=char_pos(grid, 'S'), target=char_pos(grid, 'E'))
    return len(shortest_path) - 1


def solve_part2(grid, graph):
    shortest_paths = nx.shortest_path(graph, target=char_pos(grid, 'E'))
    path_lengths_from_a = [len(shortest_paths[path]) for path in shortest_paths if grid[path[0]][path[1]] == 'a']
    return min(path_lengths_from_a) - 1


input_grid = read_input()
generated_graph = generate_graph(input_grid)
print(f"Part 1 answer: {solve_part1(input_grid, generated_graph)}")
print(f"Part 2 answer: {solve_part2(input_grid, generated_graph)}")
