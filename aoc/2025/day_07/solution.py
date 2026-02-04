"""
Advent of Code 2025
--- Day 7: Laboratories ---
"""

from pathlib import Path
from aoc.utils.parsing import read_text_grid_from_file
from collections import deque

def part1(puzzle_input):
    m, n = len(puzzle_input), len(puzzle_input[0])
    q = deque()
    s_x = puzzle_input[0].index('S')
    seen = {(0, s_x)}
    seen_splitters = set()
    q.append((0, s_x))
    while q:
        p_y, p_x = q.popleft()
        if 0 <= p_y < m-1 and 0 <= p_x < n:
            if puzzle_input[p_y + 1][p_x] == '.':
                q.append((p_y+1, p_x))
                seen.add((p_y+1, p_x))
            elif puzzle_input[p_y + 1][p_x] == '^':
                seen_splitters.add((p_y+1, p_x))
                for y, x in [(p_y+1, p_x-1), (p_y+1, p_x+1)]:
                    if (y, x) not in seen:
                        q.append((y,x))
                        seen.add((y,x))
    return len(seen_splitters)


def part2(puzzle_input):
    m, n = len(puzzle_input), len(puzzle_input[0])
    s_x = puzzle_input[0].index('S')
    ways = [0]*n
    ways[s_x] = 1

    for y in range(m-1):
        next_ways = [0]*n
        row_below = puzzle_input[y+1]
        for x, count in enumerate(ways):
            if count == 0:
                continue
            cell = row_below[x]
            if cell == '.':
                next_ways[x] += count
            elif cell == '^':
                if x - 1 >= 0:
                    next_ways[x - 1] += count
                if x + 1 < n:
                    next_ways[x + 1] += count
        ways = next_ways
    return sum(ways)


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_text_grid_from_file(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()