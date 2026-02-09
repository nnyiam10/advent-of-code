from pathlib import Path
from aoc.utils.parsing import read_lines
from collections import defaultdict
from functools import cache

def create_graph(puzzle_input):
    graph = defaultdict(list)
    n = len(puzzle_input)
    for i in range(n):
        device, outputs = puzzle_input[i].split(':')
        graph[device] = outputs.strip().split(' ')
    return graph


def part1(puzzle_input):
    graph = create_graph(puzzle_input)

    @cache
    def count_paths(u):
        if u == "out":
            return 1
        return sum(count_paths(v) for v in graph.get(u, []))

    return count_paths("you")


def part2(puzzle_input):
    graph = create_graph(puzzle_input)

    @cache
    def count(u, mask):
        if u == "dac":
            mask |= 1
        if u == "fft":
            mask |= 2
        if u == "out":
            return 1 if mask == 3 else 0
        return sum(count(v, mask) for v in graph.get(u, []))
    return count("svr", 0)


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()