"""
Advent of Code 2025
--- Day 2: Gift Shop ---
"""

from pathlib import Path
from aoc.utils.parsing import read_raw

def part1(puzzle_input):
    ranges = puzzle_input.split(",")
    total = 0
    for r in ranges:
        low_str, high_str = r.split("-")
        low, high = int(low_str), int(high_str)
        for val in range(low, high+1):
            str_val = str(val)
            if len(str_val) % 2 == 0 and str_val[:len(str_val)//2] == str_val[len(str_val)//2:]:
                total += val
    return total

def is_repeated(s):
    n = len(s)
    for d in range(1, n//2+1):
        if n % d != 0:
            continue
        k = n//d
        if k >= 2 and s == s[:d] * k:
            return True
    return False

def part2(puzzle_input):
    ranges = puzzle_input.split(",")
    total = 0
    for r in ranges:
        low_str, high_str = r.split("-")
        low, high = int(low_str), int(high_str)
        for val in range(low, high+1):
            str_val = str(val)
            if is_repeated(str_val):
                total += val
    return total


def main():
    input_path = Path(__file__).parent / "input.txt"
    puzzle_input = read_raw(input_path)

    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()