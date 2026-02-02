"""
Advent of Code 2025
--- Day 4: Printing Department ---
"""

from pathlib import Path
from aoc.utils.parsing import read_text_grid_from_file

def part1(puzzle_input):
    total = 0
    dir = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]
    m, n = len(puzzle_input), len(puzzle_input[0])
    for i in range(m):
        for j in range(n):
            if puzzle_input[i][j] == "@":
                surrounding = 0
                for dx, dy in dir:
                    if (0 <= i+dx < m and 0 <= j+dy < n) and puzzle_input[i+dx][j+dy] == "@":
                        surrounding += 1
                if surrounding < 4:
                    total += 1
    return total


def part2(puzzle_input):
    first_pass, total = True, 0
    removed_not_null = False
    removed = []
    while first_pass or removed_not_null:
        removed_not_null = False
        dir = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(puzzle_input), len(puzzle_input[0])
        for i in range(m):
            for j in range(n):
                if puzzle_input[i][j] == "@":
                    surrounding = 0
                    for dx, dy in dir:
                        if (0 <= i+dx < m and 0 <= j+dy < n) and puzzle_input[i+dx][j+dy] == "@":
                            surrounding += 1
                    if surrounding < 4:
                        total += 1
                        removed.append((i, j))
        
        if removed:
            removed_not_null = True
            for a, b in removed:
                puzzle_input[a][b] = '.'
            removed = []
        
        if first_pass:
            first_pass = False
    return total
        

def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_text_grid_from_file(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()