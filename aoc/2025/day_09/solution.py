from pathlib import Path
from aoc.utils.parsing import read_lines
from collections import defaultdict

def part1(puzzle_input):
    n = len(puzzle_input)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = [int(x) for x in puzzle_input[i].split(',')]
            x2, y2 = [int(x) for x in puzzle_input[j].split(',')]
            max_area = max(max_area, (abs(x2-x1)+1)*(abs(y2-y1)+1))
    return max_area

def intersects_with_boundary(x1, y1, x2, y2, boundary_edges):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for (edge_x1, edge_y1, edge_x2, edge_y2) in boundary_edges:
        min_edge_x, max_edge_x = min(edge_x1, edge_x2), max(edge_x1, edge_x2)
        min_edge_y, max_edge_y = min(edge_y1, edge_y2), max(edge_y1, edge_y2)
        if (min_x < max_edge_x) and (max_x > min_edge_x) and (min_y < max_edge_y) and (max_y > min_edge_y):
            return True
    return False


# Need to check, but I think this only works for convex boundaries
def part2(puzzle_input):
    n = len(puzzle_input)
    boundary_edges = set()
    for i in range(n):
        x1, y1 = [int(x) for x in puzzle_input[i].split(',')]
        x2, y2 = [int(x) for x in puzzle_input[(i+1) % n].split(',')]
        boundary_edges.add((x1,y1,x2,y2))

    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = [int(x) for x in puzzle_input[i].split(',')]
            x2, y2 = [int(x) for x in puzzle_input[j].split(',')]
            curr_area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
            if curr_area > max_area and not intersects_with_boundary(x1, y1, x2, y2, boundary_edges):
                max_area = max(max_area, curr_area)
    return max_area


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()