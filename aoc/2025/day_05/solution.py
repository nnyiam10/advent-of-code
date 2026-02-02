"""
Advent of Code 2025
--- Day 5: Cafeteria ---
"""

from pathlib import Path
from aoc.utils.parsing import read_lines

def part1(puzzle_input):
    total = 0
    lower = []
    upper = []
    for input in puzzle_input:
        if "-" in input:
            l, r = input.split("-")
            lower.append(int(l))
            upper.append(int(r))
        elif input:
            for lb, ub in zip(lower, upper):
                if lb <= int(input) <= ub:
                    total += 1
                    break
    return total



def part2(puzzle_input):
    intervals = []
    for input in puzzle_input:
        if "-" in input:
            l, r = input.split("-")
            intervals.append([int(l), int(r)])
    
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > merged_intervals[-1][1]:
            merged_intervals.append(intervals[i])
        else:
            if intervals[i][0] <= merged_intervals[-1][1] and intervals[i][1] > merged_intervals[-1][1]:
                merged_intervals[-1][1] = intervals[i][1]
    
    total = 0
    for l, r in merged_intervals:
        total += r-l+1
    return total


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_lines(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()