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


def solve_part1():
    grid = read_input()
    graph = generate_graph(grid)
    shortest_path = nx.shortest_path(graph, source=char_pos(grid, 'S'), target=char_pos(grid, 'E'))
    return len(shortest_path) - 1


print(f"Part 1 answer: {solve_part1()}")
